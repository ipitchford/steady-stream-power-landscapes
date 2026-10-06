#!/usr/bin/env python3
"""Replay all seven suites in disposable copies; preserve frozen evidence bytes."""
from pathlib import Path
import tempfile,shutil,subprocess,sys,json,importlib.metadata,platform,os
ROOT=Path(__file__).resolve().parents[1]
def main():
    versions={}
    for line in (ROOT/'requirements.txt').read_text().splitlines():
        if not line or line.startswith('#'):continue
        name,expected=line.split('==');actual=importlib.metadata.version(name)
        if actual!=expected:raise RuntimeError(f'Pinned dependency mismatch: {name}: {actual} != {expected}')
        versions[name]=actual
    rows=[]
    scripts=['verify.py','verify_structural.py','verify_extensions.py','verify_compatibility.py','verify_nonradial.py','verify_global_bounds.py','verify_negative_controls.py']
    with tempfile.TemporaryDirectory(prefix='landscape-replay-') as td:
        target=Path(td)
        for folder in ['code','data']:shutil.copytree(ROOT/folder,target/folder)
        (target/'results').mkdir()
        env={**os.environ,'OPENBLAS_NUM_THREADS':'1','OMP_NUM_THREADS':'1','VECLIB_MAXIMUM_THREADS':'1'}
        for script in scripts:
            args=[sys.executable,*(['-O'] if sys.flags.optimize else []),str(target/'code'/script)]
            proc=subprocess.run(args,capture_output=True,text=True,env=env)
            if proc.returncode:raise RuntimeError(script+' failed\n'+proc.stdout+'\n'+proc.stderr)
            rows.append({'script':script,'exit_code':0})
    print(json.dumps({'status':'PASS','python':platform.python_version(),'optimized':bool(sys.flags.optimize),'pinned_versions':versions,'checks':rows,'scope':'Producer-side computational checks, not proof certification or independent reproduction.'},indent=2))
if __name__=='__main__':main()

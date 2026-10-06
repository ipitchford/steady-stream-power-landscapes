#!/usr/bin/env python3
"""Deliberate corruptions must be rejected in normal and optimized Python."""
from pathlib import Path
import tempfile, subprocess, sys, json
ROOT=Path(__file__).resolve().parents[1]
def main():
    outcomes=[]
    with tempfile.TemporaryDirectory(prefix='landscape-negative-') as d:
        d=Path(d)
        source=(ROOT/'code/verify.py').read_text()
        token='sp.Rational(2,5)-x*x/10-2*y*y/5'
        if token not in source:raise RuntimeError('Mutation anchor missing')
        changed=source.replace(token,'sp.Rational(2,5)-x*x/9-2*y*y/5',1)
        script=d/'wrong_torsion.py';script.write_text(changed)
        coefficients=json.loads((ROOT/'data/ellipse-coefficients-v1.2.json').read_text())
        for row in coefficients['records']:
            if row['degree_parameter']==4 and row['K']==.2:row['coefficients'][0]+=1
        damaged=d/'wrong_coefficients.json';damaged.write_text(json.dumps(coefficients))
        omitted=d/'missing_degree.json'
        low=next(r for r in coefficients['records'] if r['degree_parameter']==2 and r['K']==.2)
        omitted.write_text(json.dumps({'records':[low,low,low]}))
        for mode in [[],['-O']]:
            for name,args,marker in [('torsion',[str(script)],'Verification failed'),('ellipse',[str(ROOT/'code/verify_global_bounds.py'),str(damaged)],'Global'),('missing-degree',[str(ROOT/'code/verify_global_bounds.py'),str(omitted)],'Global coverage')]:
                run=subprocess.run([sys.executable,*mode,*args],capture_output=True,text=True)
                if run.returncode==0 or marker not in run.stderr:raise RuntimeError('Negative control was not rejected for expected reason: '+name)
                outcomes.append({'mutation':name,'optimized':bool(mode),'rejected':True,'exit_code':run.returncode,'reason':run.stderr.splitlines()[-1]})
    result={'status':'PASS','controls':outcomes,'scope':'Detects these identity and polynomial corruptions, not arbitrary errors in analytical PDE proofs.'}
    (ROOT/'results/negative_controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()

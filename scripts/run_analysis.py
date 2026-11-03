"""One entry point: rebuild the frozen study's data products, statistics and plots."""
import subprocess
import sys
from common import ROOT

def main():
    for name in ['export_data','clean_data','feature_engineering','analyze_accuracy','summarize_timing','power_analysis','make_figures','validate']:
        subprocess.run([sys.executable,str(ROOT/'scripts'/f'{name}.py')],check=True,cwd=ROOT)
    print('Complete: see results/, presentation/ and docs/analysis_interpretation.md')

if __name__ == '__main__':
    main()

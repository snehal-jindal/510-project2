"""Publication-style figures drawn from generated features/results, not typed scores."""
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.ticker import PercentFormatter
from scipy.stats import binom
from common import ROOT, load_features, read_csv

OUT=ROOT/'results/figures';OUT.mkdir(parents=True,exist_ok=True)
FG='#F4F6F8';MUTED='#A0AAB7';GRID='#27303B';CYAN='#57E6D5';AMBER='#FFBA80';SLATE='#8897AC';DARK='#303A48'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':14,'figure.facecolor':'black',
    'axes.facecolor':'black','savefig.facecolor':'black','text.color':FG,'axes.labelcolor':MUTED,
    'xtick.color':MUTED,'ytick.color':FG,'axes.edgecolor':GRID,'axes.spines.top':False,
    'axes.spines.right':False,'axes.spines.left':False})

def save(fig,name):
    fig.savefig(OUT/f'{name}.png',dpi=240,facecolor='black')
    plt.close(fig)

def main():
    rows=load_features();r=json.loads((ROOT/'results/statistical_results.json').read_text())
    counts=r['paired_counts'];n=r['n_pairs']
    fig=plt.figure(figsize=(9.4,3.1));ax=fig.add_axes([.21,.23,.72,.67])
    for y,who,color in [(1,'human',CYAN),(0,'ai',AMBER)]:
        lo,hi=r[who+'_accuracy_wilson_95'];p=r[who+'_accuracy']
        ax.hlines(y,lo*100,hi*100,color=color,lw=4)
        ax.vlines([lo*100,hi*100],y-.075,y+.075,color=color,lw=2)
        ax.scatter(p*100,y,s=145,color=color,zorder=3)
        ax.text(p*100,y+.21,f'{p:.0%}',ha='center',fontsize=21,color=color,weight='bold')
        ax.text(-8,y,who.title() if who=='human' else 'AI',ha='right',va='center',fontsize=18)
        ax.text(-8,y-.21,f'{r[who+"_correct"]}/{n} correct',ha='right',fontsize=12,color=MUTED)
    ax.set(xlim=(0,100),ylim=(-.48,1.55),yticks=[],xticks=[0,25,50,75,100],xlabel='Whole-code accuracy (%)')
    ax.grid(axis='x',color=GRID,lw=.7);ax.set_axisbelow(True)
    fig.text(.93,.96,'95% Wilson intervals',ha='right',va='top',fontsize=12,color=MUTED)
    save(fig,'accuracy')

    fig=plt.figure(figsize=(6,3.45));ax=fig.add_axes([.015,.32,.97,.65]);ax.set_aspect('equal')
    colors=[SLATE]*counts['both_correct']+[CYAN]*counts['human_only']+[AMBER]*counts['ai_only']+[DARK]*counts['neither_correct']
    for i,color in enumerate(colors):
        ax.add_patch(Rectangle((i%10+.08,4-i//10+.08),.84,.84,facecolor=color))
    ax.set(xlim=(0,10),ylim=(0,5));ax.axis('off')
    labels=[(SLATE,f'{counts["both_correct"]} both correct'),(CYAN,f'{counts["human_only"]} human only'),(AMBER,f'{counts["ai_only"]} AI only'),(DARK,f'{counts["neither_correct"]} neither correct')]
    for i,(color,label) in enumerate(labels):
        x=.04+(i%2)*.5;y=.21-(i//2)*.12
        fig.add_artist(Rectangle((x,y-.013),.027,.045,transform=fig.transFigure,facecolor=color))
        fig.text(x+.045,y,label,fontsize=14,va='center')
    save(fig,'paired_outcomes')

    b=counts['human_only'];m=b+counts['ai_only'];k=np.arange(m+1)
    fig=plt.figure(figsize=(6.1,3.45));ax=fig.add_axes([.18,.22,.78,.71])
    ax.bar(k,binom.pmf(k,m,.5),color=[AMBER if v>=b else SLATE for v in k],width=.78,zorder=3)
    ax.axvline(b,color=AMBER,lw=1,ls='--');ax.text(b+.4,.122,f'Observed: {b}',fontsize=14,color=AMBER)
    ax.set(xlim=(-.7,m+.7),xticks=[0,5,10,15,20,m],xlabel=f'Human-only wins among {m} disagreements',ylabel='Probability')
    ax.yaxis.set_major_formatter(PercentFormatter(1,decimals=0));ax.grid(axis='y',color=GRID,lw=.7)
    save(fig,'exact_test_null')

    shared=[row for row in rows if int(row['shared_success_timing_eligible'])]
    fig=plt.figure(figsize=(5.7,3.3));ax=fig.add_axes([.19,.24,.77,.68])
    for y,who,color in [(1,'human',CYAN),(0,'ai',AMBER)]:
        x=np.array([float(row[who+'_time_seconds']) for row in shared])
        ax.boxplot([x],positions=[y],vert=False,widths=.27,patch_artist=True,showfliers=False,
            boxprops={'facecolor':color,'edgecolor':color,'alpha':.18},medianprops={'color':color,'linewidth':2.4},
            whiskerprops={'color':color},capprops={'color':color})
        jitter=np.empty(len(x));jitter[np.argsort(x,kind='stable')]=np.linspace(-.13,.13,len(x))
        ax.scatter(x,y+jitter,s=24,color=color,zorder=4)
    ax.set(yticks=[1,0],yticklabels=['Human','AI'],xlim=(0,40),ylim=(-.5,1.5),xticks=[0,10,20,30,40],xlabel='Recorded seconds')
    ax.grid(axis='x',color=GRID,lw=.7);save(fig,'timing_descriptive')

    power=read_csv(ROOT/'results/power_curve.csv')
    fig=plt.figure(figsize=(6.2,3.55));ax=fig.add_axes([.18,.22,.78,.72])
    ax.plot([int(x['n']) for x in power],[float(x['power']) for x in power],color=CYAN,lw=3)
    ax.axhline(.8,color=FG,lw=1,ls='--')
    for nn,color in [(50,CYAN),(67,FG)]:
        p=next(float(x['power']) for x in power if int(x['n'])==nn)
        ax.scatter(nn,p,color=color,s=70,zorder=5);ax.vlines(nn,0,p,color=color,alpha=.3)
    ax.set(xlim=(10,140),ylim=(0,1.02),xticks=[10,50,67,100,140],xlabel='Number of matched image pairs',ylabel='Power')
    ax.yaxis.set_major_formatter(PercentFormatter(1,decimals=0));ax.grid(axis='y',color=GRID,lw=.7)
    save(fig,'power_planning')

    # This post hoc descriptive figure is deliberately not presented as a causal test.
    groups=read_csv(ROOT/'results/exploratory_digit_groups.csv')
    fig,ax=plt.subplots(figsize=(8,4),layout='constrained');xx=np.arange(len(groups))
    for offset,who,color in [(-.16,'human',CYAN),(.16,'ai',AMBER)]:
        ax.bar(xx+offset,[int(g[who+'_correct'])/int(g['n']) for g in groups],width=.3,color=color,label=who.title())
    ax.set(xticks=xx,xticklabels=[f'{g["digit_count"]} digits\n(n={g["n"]})' for g in groups],ylim=(0,1.05),ylabel='Accuracy',title='Exploratory: digit groups were not randomized')
    ax.yaxis.set_major_formatter(PercentFormatter(1));ax.legend(facecolor='black',labelcolor=FG)
    save(fig,'digit_mix_exploratory')

if __name__ == '__main__':
    main()

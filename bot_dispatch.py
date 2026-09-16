"""Controller selection shared by experiments and sampled continuations."""
from shared_sim import choose,policy_for

def select_order(a,p,phase,policies,decision,horizon=0):
    if p in a.human_players:raise ValueError('Human orders cannot be generated')
    mode=getattr(a,'bot_controller_modes',{}).get(p,'operational')
    policy=policy_for(a,p,policies)
    if mode=='tactical':return choose(a,p,phase,policy,decision)
    if mode=='diagnostic':
        from siege_diagnostic import SiegeDiagnostic
        bot=SiegeDiagnostic();bot.targets=getattr(a,'diagnostic_targets',{})
        order=bot.select(a,p,phase,policy,decision);a.diagnostic_targets=bot.targets
        return order
    if mode!='operational':raise ValueError('Unknown controller '+mode)
    if horizon:
        from operational_search import plan
        return plan(a,p,phase,policies,decision,horizon)
    from operational_bots import select
    return select(a,p,phase,policy,decision)

## Current source consolidated - 6 October 2026

User requested the source be brought into line with the current rules and reread in full. Source_Rules_Playtest_2026-10-06.md is the current playtest edition, using decision-recovery-package-20261006/candidate (Efficient8, other11 unchanged). Reconciled all12traits,33construction profiles and action/combat/resource/setup rules; updated the five templates/guides and library builder. Reconciliation and known simulator coverage differences: Source_Reconciliation_2026-10-06.txt. Verification: source-reconciliation-checks.json. Local source page and dated ZIP rebuilt; no GitHub publication claimed. Historical baseline, frozen studies and Dessica unchanged. No new batch or timer. Current source supersedes older status/proposal text below; Atreus remains unopened.


## Decision and recovery package inspected — 6 October 2026

200 new candidate games and 200 saved controls completed without failures; 289,596 combined replay-validated orders. Full manual review and paired initial-state checks complete. Report: decision-recovery-package-20261006/Full_Manual_Inspection_2026-10-06.txt. Recommend candidate for Atreus playtest under the user-approved same-or-better overall criterion, even outside25pp; recommendation only, no automatic promotion. Spread32→28pp; mean56.51→55.825Cycles; shortages892→943 with Supply exposure4.795→5.299%, Manpower3.888→4.166%. Construction delivery almost unchanged; Scouts improve, support stations remain poor. Case57 strike/repair loop resolves, but case161 retains39Cycles without combat. No claim of perfect bot coordination or human Soulstorm win-rate prediction. Atreus roster uses Efficient8, War6Supply/logistics, Martial4Manpower/logistics if candidate selected; pooled rates50/22/22 are not a forecast for that trio. Next work: consolidate selected source version and finish Atreus setup; no new batch scheduled. Root baseline and Dessica unchanged.

## 6 October 2026 — Decision/recovery package QUALIFIED and RUNNING

Directory decision-recovery-package-20261006. Runner PID25660;started2026-10-06T20:20:45.0284239+11:00. Two workers,200NEWcandidate games versus200exact-input reused fresh-confirmation controls;50appearances/trait/arm. Three-hour dispatch limit;finishactivegames/checkpoint if reached. ETA2.5–3hours from20:20Sydney (roughly22:50–23:20);no timer orautomaticfollow-on. Checkmanifest,worker-status,progress,errors;do notduplicate. Sourcefresh200controls have32ppspread,target25. This schedule is now developmental because its savedstates informed fixes;not independent confirmation.

OnlytraitrulechangeEfficientReinforce/Muster9→8. Other11traitrules fixed. Bots: Scoutcombineswithpresentdestination support,finishesviableexistingworkbeforeseedingandcanreplaceineffectivework;compareoptionalnon-economicrepairswithfundedBuild;damagedconvoyarrivalvsindividualsafety;three-observationrepairedstructurefallbackguard;next-operationresourcefunding;correctstaleVoidfree-expansionforecasts. No constructionpricechange/humanDifficulty/automaticMobileloss.

662regressiontests+6edges pass;72savedstates,144legalchoices,6250verifiedhistoricalprefixorders;9changedchoices. Cases7/161 nowchoosepaidScoutat85. Case57C100 twoBuildactionsfor6SupplyactivateSystemRepair,nextPhase0+3Strength (isolatedconditionalcheck,noenemy/events);fleetsalsochooseyardconvoyoveridle. Resourceguard passesfocusedtestsbutnochangedWar/Martialdecisioninsampled witnesses: donotclaimweaknessresolved. Preparation_Findings_2026-10-06.txt,QUALIFICATION_COMPLETE.json,targeted-witness-checks.json. Failedinterimchecksresolvedwithdocumentedrule-expectationupdates;finalpass.

All execution inputs frozen includingnewdecision_recovery.py. Studyauto-summarisesandstructurallyinspects after400records(200reused+200new),thenneedsfullmanualinspection. Rootbaselineunchanged,Dessicauntouched,nopublication/promotion. EarlierRUNNINGentrieshistorical.

## 6 October 2026 — Fresh confirmation FULL INSPECTION COMPLETE; observed gate failed

200 NEW games, 145,168 replay-validated orders, no errors/censoring. Same frozen engine/bots as income-investment candidate; no new changes this inspection. Fresh trait spread32pp fails25pp target: Efficient52,Dread44,Salvagers40,Fort38,Industrial36,Siege/Endurance/Swift32,Void26,Mobile/Martial24,War20. Earlier16pp development result is not a different ruleset to revert to and must not be cherry-picked. Fifty appearances per trait; map/seat checks do not explain Efficient/War gap. Efficient blocks56/48,War28/12; Fort24/52 shows residual noise.

Mean56.51/median55;117/200 in50–100. Five >100 all Mobile; cases7/161 have33/38 combat-free Cycles, case57 ends via storm after repeated construction attacks/repairs. Shortages892; no illegal voluntary deficits; Supply/MP exposure4.80/3.89%. Construction10,773/31,490 Supply(34.21%)neveractive;Storm30/400,SystemDefence1/82,SystemRepair2/96active. Nine profiles unpurchased. All12traits and routes inspected; no human Soulstorm odds inferred.

Report fresh-confirmation-20261006/Full_Manual_Inspection_2026-10-06.txt and MANUAL_INSPECTION_COMPLETE.json. Recommendations ONLY: qualify Efficient9→8;hold11othertraits; saved-state resource-policy, construction-continuation and terminal-pursuit corrections before any combined new run. War shortages18S/41MP,Martial45S/23MP: do not blindly buff the resource each already has. No implementation/newrun/timer/publishing/promotion. Root baseline hash unchanged;Dessica untouched. Await user direction. Earlier RUNNING entries historical.

## 6 October 2026 — Frozen candidate FRESH CONFIRMATION RUNNING

Directory fresh-confirmation-20261006; runner PID26564,started2026-10-06T17:04:53.8012865+11:00.200NEWgames,two workers,no reusedcontrols,50appearances pertrait,25permapfamily,16trait-led pertrait. New fixed event/map seeds; same roster coverage with rotated second-blockseats and reversedmapfamilies. All execution-input hashes identical to income-investment-package-20261006/candidate; inherited653regressions+6edges. No trait or bot changes. This is independent scenario confirmation,not a new ruleset or a paired improvement experiment.

User authorised proceeding and intends playtest if satisfactory. Clarified there is no newrulesversion to revert from: retain current16ppdevelopmentcandidate and examine fresh evidence if worse. Do not cherry-pick the better sample or retune midrun. Expected2.5–3hours from17:05Sydney (around19:35–20:05).3hourdispatchlimit finishesactivegames/checkpoints ifneeded. No timers,auto-follow-on,publishing orbaselinepromotion.

Checkmanifest,worker-status,progress,runner-errors. Do notduplicate. Summary and structuralinspection automaticafter200games;fullmanualverdictstillrequired. Inspectall12traits25ppspread,duration50–100,Mobilepursuitgaps,shortageexposure,constructiondelivery,routes. RootbaselineandDessicasuspendedCycle21unchanged. Earlierbatchentrieshistorical.

## 6 October 2026 — Income/investment FULL INSPECTION COMPLETE; observed target met

All100new+100reusedgames valid,143702replayedorders,100pairedstates and reuse/frozenhashes pass. Spread32->16pp,target25:War/Salvagers/Swift40,Dread36,Mobile/Efficient/Siege/Void/Fortification/Martial32,Endurance28,Industrial24. Development sample25appearances/trait,not independent confirmation. Freeze current package; recommend200fresh games(two workers,roughly2.5–3hours) when authorised. No new run or rule edits this inspection.

Median55,mean56.55,61within50–100;37shorter,twoMobile endings129/161Cycles. Case25no combat105–143;Scout149–153thenattacks154–161. Pursuit not fully solved. Deficits365->425,lockedexposureSupply4.42%,MP3.75%;zeroillegalvoluntaryself-deficits. Worstcase50all9entriescombat,zerorecentconstruction. ConstructionneveractiveSupply5612->4998,share32.75->30.57%;StormTransit17/194active,107unfinished,still weak. Dreadcase18expands1->29,ground3->28;trait-ledoverall1/8. Nineprofilesunpurchased. No claim fullconstruction or humanSoulstormbalance proven.

Full report:income-investment-package-20261006/Full_Manual_Inspection_2026-10-06.txt;MANUAL_INSPECTION_COMPLETE.json. Rootbaseline/Dessica preserved,no publishing/timer/promotion. EarlierRUNNING entries are historical;batch andinspection complete.

## 6 October 2026 — Income/investment package qualified and RUNNING

Started 2026-10-06T12:57:06.0503460+11:00, runner PID13492, directory income-investment-package-20261006. Two workers,100NEWcandidategames vs100exact-input reused followup-package controls;25appearances/trait/arm. Three-hour dispatch limit, checkpoint if reached. ETA90–120minutes from12:57Sydney (about14:27–14:57); previousbatch71minutes. No timers or automatic follow-on. Check manifest,worker-status,progress and runner-errors; do not duplicate.

War Economy +6 Supply/Logistics instead+8; general safe refit fallback corrects Dread's demonstrated idle expansions; Efficient planning yield7 corrected9; Storm Transit forecasts no current-event protection and no benefit from visibly departing fleets. Other rules/prices unchanged. 653tests+6edges pass;6390historicprefixorders verified,43savedstates/86legalchoices,4choicechanges. Synthetic33profile/4context and10alternative/400dicepair comparisons retained. Weak/unusedconstructions are not declared fixed; no arbitrary discounts.

See Preparation_Findings_2026-10-06.txt, QUALIFICATION_COMPLETE.json and Income_Investment_Rules_2026-10-06.txt inside candidate. Previous32ppspread stillfails25; no results yet. On completion run full manual inspection, including corrected refit usage and construction completion. Rootbaseline hash unchanged; Dessica remains suspended; no publication/promotion.

## 6 October 2026 — Followup package full inspection COMPLETE

100 new candidate games plus 100 exact reused controls, 144,762 replay-validated orders; paired states, frozen hashes and reuse provenance pass. No failures/censoring. Observed spread improves 40 -> 32 percentage points but fails the 25-point target. War 56%; Salvagers 44%; Swift 40%; Mobile/Fortification/Industrial/Martial 32%; Efficient/Siege/Endurance 28%; Void/Dread 24%. All eleven except War fit a 20-point band. Development sample: 25 appearances per trait, not fresh confirmation.

Mean 56.35 Cycles, median 53.5; 55 in 50–100, 44 shorter, one longer (107, active territorial war). Deficits 365 versus 381. Never-active construction Supply share 32.75% versus 30.40%, although absolute waste falls 5689 -> 5612. Carrier/Storm Transit/Repair Tender completion remains weak; ten profiles unpurchased. Dread trait-led remains 0/8 despite functioning attack tax. Case26 shortening is a winner change, not Scout success; cases46/56 end with Scout-assisted attacks.

Report: followup-package-20261006/Full_Manual_Inspection_2026-10-06.txt; evidence certificate MANUAL_INSPECTION_COMPLETE.json. Recommendations only: retain current candidate; propose War +6 instead of +8; inspect Dread creation/expansion decisions and construction interruption/value in saved states, then combine supported changes before another paired run. No rules changed, campaigns started, publication, baseline promotion or Dessica edits. Root simulator hash unchanged. No runner remains to monitor. Prior RUNNING entries below are historical.

## 6 October 2026 — Approved followup package qualified and RUNNING

RunnerPID16172, started2026-10-06T11:02:39.901908+11:00. Directoryfollowup-package-20261006. Two workers100NEWcandidate games vs100reused exact-input previouscandidate controls (combined-preflight-20261005);25appearances/trait/arm,100matched developmental scenarios. Userapprovedproceeding,three-hourdispatchlimitretained. Checkmanifest/worker-status/progress/errors; donotduplicate. No timer,automatic follow-on,publishing orbaselinepromotion.

ImplementedFortfreeDefend4/Defendedwith2S0MP;VoidremoteExpand4for1S1MP;EfficientReinforce/Muster9. Fortbot usesactualnewgrants;Dreadtrait-led balancedwhenresources>=8andnoemergency/deficit,otherwiseconservative; terminalchasefundedScoutselectionrequiresdamageoutpacingrepairorlethality. Allothertraitsheld,Martial/unusedconstructionpricesunchanged. Scouthostcomparisoncase26C100old5damagevs6repair,new8damagevs6repair; notyetprovenwholecampaignchasefix.

Qualification645regressiontests+6edgechecks,5557exactprefixorders,63savedstates/126legalchoices. Paidconditionalconstructioncomparisons400dicepairsx10alternatives,notnewcampaigns, excludesconstructiondelay. Preparation_Findings_2026-10-06.txt andQUALIFICATION_COMPLETE.json. Originalstudy/control/baseline/Dessicaunchanged. ETA1.5–2.5hours fromlaunch;3hourdispatchcutofffinishesactivegamessafelythencheckpointsifneeded. Automaticfullstructuralinspectionfollowedbymanualverdictrequired. Reuseddevelopmentdata,notfreshconfirmation; target25ppnotyetmet(previous40pp).

## 6 October 2026 — Combined package full inspection COMPLETE; target not met

100new+100reusedcontrolgames,147136orders,allpairedinitials/frozenhashes/controlprovenance verified; nofailures/censoring. Spread56->40pp(target25). Rates:Void/Fort56,Salvage48,Industrial40,War36,Siege32,Swift28,Mobile/Endurance24,Dread/Martial20,Efficient16. Mean57.98,54within50–100,6over100allMobile. Case26no combat60->132; pursuitnotfixed. Deficits395->381; worstcase28extra9shortageshaszerorecentconstructionatallentries. StormretentionimprovesbutoverallneveractiveSupply30.13->30.40%. Fortification463/1170Defendsatfullhealth,0Reinforce.

Report:combined-preflight-20261005/Full_Manual_Inspection_2026-10-06.txt; MANUAL_INSPECTION_COMPLETE.json. Proposed ONLY:FortDefendgrant2S0MP(instead3S1MP),VoidExpand1S1MP(retainremote+4/upkeep),Efficientactions9(instead7). Holdothertraits; qualifyDread/MartialpolicyandMobileinterception plusunusedconstructionmarginalvalueinsavedstatesbeforecampaign. Dreadalreadytaxes1813eachresource;Martial23Supplyvs5MPdeficitsmeansmoreMPnotobviousfix. Userapprovalneededfornextimplementation. Nochanges,newbatch,timer,publishingorDessicaeditduringinspection. Donotclaim40ppisatargetpassorhumanbalanceproof.

## 5 October 2026 — Combined matched comparison RUNNING

Started 2026-10-05T21:35:57.587247+11:00, runner PID9692 in combined-preflight-20261005/run_combined.py. User approved proceeding and raised limit to3hours. Two workers,100 newly simulated candidate games,100 reused exact-input prior candidate games as control,100 matched scenarios,25 appearances/trait/arm. Prior control replay results and trace hashes preserved in reused-control-provenance.json; no claim of200new games. ETA1.5–2.5hours based on previous two-worker throughput, variable with long campaigns. Dispatch stops after3hours; active games finish safely, incomplete runs checkpoint without automatic restart. No timers.

Check manifest.json,worker-status.json,progress.txt,runner-errors.txt; never duplicate runner. Each new game replay-validates. Automatic summary/full structural inspection runs after all100newgames; manual interpretation remains required. Package includes rules AND planning changes so do not attribute all paired changes to traits alone. Development schedule reused,not independent holdout. Original study/root baseline/Dessica unchanged. No automatic follow-on batch or publication.

## 5 October 2026 — Combined package prepared; no campaign batch started

Approved War +8, Mobile 60% intrinsic combat, Dread +1 each-resource surcharge, Siege up-to1 base Supply victory refund implemented in isolated combined-preflight-20261005/candidate. Construction retention and trait-aware assault/pursuit planning added. Control and prior study unchanged; root baseline hash verified.

635 regression tests plus6 edge checks pass; 5335 original orders exactly replay-verified;40 saved situations yield80 legal counterfactual decisions. Two construction choices improve retention; sampled fleet decisions unchanged, so Mobile duration improvement remains unproven. All33 profiles reviewed in4 synthetic equal-budget contexts:12 zero-purchase profiles still weak/rejected under current valuation. Regeneration deadlock hypothesis disproved by4 direct base/upgrade checks; positive-Integrity exception already works. Flagged deficit is battle casualties after affordable payment, not illegal spending.

Full report: combined-preflight-20261005/Preflight_Findings_2026-10-05.txt. Frozen manifest: QUALIFICATION_COMPLETE.json. Ready for a separately started matched comparison, NOT a balance-target pass. No new campaigns, timer, publication or Dessica edits. Construction value needs focused marginal-outcome evidence before blanket price changes. Previous56pp spread is historical, not a result of this package.

## 5 October 2026 — 200-game comparison manually inspected; not within trait target

Completed all 200 games / 100 matched pairs at 18:35 Sydney; 142,053 replay-validated orders. Additional all-trace audits verify frozen hashes, finals, 100 paired initial states and 39 unaffected identical outcomes. Report: dual-worker-study-20261005/Full_Manual_Inspection_2026-10-05.txt; evidence manual-audit.json and mechanism-audit.json. Manual inspection now complete; no new batch or rules changes. Root baseline unchanged.

Spread 72 -> 56pp, fails25pp target. Candidate wins/25: War18, Void13, Fortification11, Salvagers10, Mobile9, Industrial8, Efficient/Endurance/Swift6, Martial5, Siege/Dread4. Mean54.07->57.16 Cycles;49 candidate within50–100,43short,8long,no censoring. Seven long games include Mobile; isolated Mobile-change scenarios4->4 wins/16 and mean+22.125Cycles. Swift isolated2->4/16; Void5->8/16 with fewerExpands/moreMuster, not a direct strength buff. War strong on both map types and across policies.

Deficit358->395, exposure rises only0.087pp Supply/0.368pp MP. Flagged case84C41 is legal2MP Dread payment from4 followed by two fleet-destruction losses; diagnostic conflates actor casualties with illegal voluntary spending. Never-active construction spend share31.18->30.13%; Storm Transit30/320 active,1205/1570 spend never active. Case25 Mobile repeatedly builds in enemy-owned systems and loses Major projects when enemy void superiority returns: correct retention forecasts/restart behaviour, not capture rules. Bombardment remains793 choices,386 with ordinary ground also in menu (not necessarily same target). Fortification458/1068 Defends on full holdings; legal economic benefit. Twelve catalogue profiles have no purchases; untested situational value remains, do not infer uselessness.

Recommendations pending approval: keep Swift1S1MP Create6 and Void0S1MP Expand4; provisionally revert Mobile70%intrinsic to control60%; War+12->+8Supply/Logistics; modest Dread1+ceil(strength/5)->2+ceil(strength/5) each resource; optional Siege victory refund1paid base Supply capped at payment, no surcharge refund or defeat buff. Siege-aware planning and unsafe system construction correction; hold other traits rather than score-chase. Qualify saved situations before any new comparison. No automatic batch/publishing/timers. AI does not predict human Soulstorm wins; unused confirmation remains reserved.

## 5 October2026 —200game/two-worker matched comparison BENCHMARK STARTED

Userexplicitlyapproved two workers for100games each;recommended100matchedscenarios/200totalgames. Directory dual-worker-study-20261005. WrapperPID19128,start15:47:45Sydney. run_parallel.py first benchmarks4scheduledjobsserialthenparallel,checksfulltrace/resultidentity,requires speedup>=1.15 andavailableRAM>=15%or4GiB,then automatically runsremaining196via shared2workerqueue. Benchmark4parallelresults counttoward200;serialduplicatesarenotadditionalindependentgames. Do not duplicate. Readworker-status.json/benchmark.json/manifest.json forphase/progress. No timers ornextbatch.

Machine16logicalprocessors,31.9GiBRAM,~20.5availableatpreflight. OS CIMdenied;read-only WindowsmemoryAPIused. Memory sampled3seconds,actualprocesspeaknotmeasured. Ifbenchmark failsgate,statusbenchmark_review_required;do notclaimentirerunstarted. InitialETAawaitsbenchmark. Enginesbyte-identicaltopreviouslyqualified reliable-testingcontrol/candidate,includingsame3changesSwift/Void/Mobile;botsidentical.616regressionsand77savedchecks inheritedbyexactfileverification,notclaimedrerun. Newqueueconcurrency/no-low-memorydispatchtestsandschedulecheckspassed.

Schedule100uniquetriples,25appearancespertraitperarm,allpairs4–5,seat8–9,map12–13,8trait-led17general(each2–3). Botharmssameinitials/seeds/policies. Reserved36scheduleuntouched. Knownmechanismlimitationsretainedtoavoidconfounding;exactsavedprefixes2193ordersreplayedforcase4C75/case8C60/case3C20/case5C15,eightstates;legaldecisions/snapshotnonmutationchecked. SavedScoutatcase4alreadycomplete,12mobileassaultoptions butnavalselected;Warcarrierpositivevaluestillconstructionnoneunderdefensiveemergency;Stormnegativevalue. Thesearenotprooffixedandmustbeinspectedinlargerresults.

Oncompletionfullmanualinspectionrequired:all12pairedwins/losses,25ppgoalwithuncertainty,50–100duration,resource/construction/route/pursuitharmflags. No historicaltuneddataasindependentconfirmation. No publishing,baselinepromotionorDessicaedits. Rootbaselinehashprotected. Frozenharnessandinputs;nevereditduringrun.

## 5 October2026 — Reliable paired screen FULL INSPECTION COMPLETE

32games/16pairs/21013orders;allresolved,replayvalidated,hashes/finals/initialconditionsverified. Sevenunaffectedpairsidenticalorders;9changedpairsdiverge. Report reliable-testing-20261005/Full_Manual_Inspection_2026-10-05.txt andmanual-pair-audit/manual-mechanism-audit.json. Separate manualmarker supersedesautomaticpending. No newbatch.

Spread75->75pp;4appearancescannotcertify25pp. WinscandidateWar/Salvagers3;Fortification/Siege/Void2;Efficient/Industrial/Mobile/Swift1;Martial/Endurance/Dread0. Winnerchanges3Void->Siege,6Martial->Swift,13Endurance->Void. Swiftcostloweringpromising(peakholdings7->13,Create14->20),Voidrefitpressureeffective(Expand112->63,MP38.41->30.40),Mobilewinflatbutcase4peak3->7/elimination29->98,latechase74–98. Do notreatmiddletraitlossesasautomaticbufforders.

Mean49.125->53.6875;within50–1007->8;nonecandidateover100. Deficits56->59,exposureincreases<0.3pp,no voluntaryselfdeficits. Constructionactivation36.27->39.04%,neveractivespendshare33.95->31.92%;case4+227of+275totalspendingduelongerwar. Carrierwaste95->176;Storm153->135. Routevarietyretained. Allpredeclaredsafety/aggregateharmflagsclear,buttraittargetnotmet.

Recommendholdthree-changecandidateprovisionally;no furthernumericchangesfromfourappearances. InspectDreadtax/WarSalvagerecovery,mobilecase4/8pursuit,Carrier/Stormdeliveryinequivalent savedpositions beforedecidingnextpackage. Keepbotsqualifiedseparately;reserved36scheduleunrun. No largerconfirmationyet,nopublishingorbaselinepromotion;Dessicapreserved.43.29minutes completedworker runtimeexcludinginterruption,notoriginalwallclock.

## 5 October2026 14:47Sydney — Reliable testing resumed after unlogged interruption

Atuserstatuscheck14:46,only3/32gamescomplete,lastsaved13:34. Originalwrapper18456/runner23356 bothabsent;stale manifestclaimedrunning,nologgederror. Causeunknown;do notclaimnormalprogressorcompletion. Frozenharness/enginehashesverified;3validatedresultsretained;interruptionmanifestandstalelockarchivedin reliable-testing-20261005. Resumedsamefrozenrunner14:47:22,wrapperPID25464,remaining29games,ETA50–65minutes approximately15:40–15:55Sydney. No duplicate/noinputsmodified. resume-launch.json records restart;originalstarted_epoch includesdowntime andmustnotbeusedasactive-runtime estimate. No timer/automation. Awaitactualcompletionbeforebalance conclusions.

## 5 October 2026 — Reliable paired testing protocol implemented;32games RUNNING

User approved reliability overhaul. Directory reliable-testing-20261005;launched13:29SydneyAEDT,wrapperPID18456.16pairedscenarios/32NEWgames,oneworker,estimated55–65minutes (14:25–14:35). No duplicate,no timer,no automaticnextbatch,no publication/baselinepromotion;Dessica preserved.

Validated shortschedule eachtrait4appearances/8distinctopponents/map2each/seat1,1,2/one trait-led+3distinctgeneralpolicies. Reserved36schedule(notrun) has9appearances/3perseat/map4–5/3trait-led+6general andall11opponents1–2times. Both schedules generated beforeoutcomes,independentlyvalidated. No claim shortsample certifies25ppspread. Sameinitialstates,seed,map,opponents,policies,bots forbotharms. Differentdecisions canconsume RNG differently. Traitpackageonly:VoidExpand0S1MP(+4remote),SwiftCreate6at1S1MP,Mobileintrinsic70%roundednearestfull12=>8. Other9unchanged. Control=freshconfirmationcandidate. Constructionbotchanges deliberately excluded to avoidconfounding.

Qualification616regressions,77saveddecisions,10savedbattlefieldoptionchecksperarm,cost/action/deficitboundaries,schedule+pairedcompletenessguards.12initialregressionfailures wereoldexpectedcosts/contributions/fingerprint,updated onlycandidateexpectations;firstoutputsretained. One wrong-working-directory regression invocation retained,correctcwdfinalallpass. Rootbaselinehash56e855e9c23a88e8122696256b71bc6f2f38fa7137470de10f1903bc0208cffc unchanged.

Read Testing_Protocol_2026-10-05.txt andStudy_Plan.txt. Predeclared safetygates andmanualflags:meanoutside50–100,pairedmean+10Cycles,eitherresourceexposure+2pp,neveractivespendshare+5pp,newcensoring,oppositedirectionaffectedtraits. Flagsnotautomaticrulechanges. Reportall12pairedgains/losses, uncertainty,duration,shortages,constructions/routes. Screeningcannotcertifyparity;reservefreshconfirmationuntilpackagefrozen. No oldgamesreusedascontrols. Manualinspectionrequiredafterautomaticpostprocess.

Reportingcaveat:copiedrunnerplanned_new_gamesfield remains16andprogressmayprint32/16 despite32actualnewgames. Actualplanned_games32,paired_scenarios16 andresultcount32governcompletion. Frozenrunnerleftunchanged;do notinterpretconsoledenominatorasextraunplannedgames. Finalsummaryseparates16perarm. No causalclaimforisolatedtraitwithincombinedpackage.

## 5 October 2026 — Fresh confirmation FULL INSPECTION COMPLETE: FAIL

36games/29721orders,allresolved/replayvalidated,no failures. Trait rules byte-identical to pursuit screen; onlytwoScoutplanningfiles changed. Freshspread66.7pp (Void6/9,Mobile0/9),vsold22.2screen. Swift1/9;War/Efficient5;Fortification/Endurance4;Industrial3;Siege/Martial/Salvagers/Dread2. Old reusedscreen was not robust confirmation. Schedule balanced seats/strategies but clustered opponents3or6meetings, someabsent,map3–6appearances; not a fully balanced tournament. No same-scenario oldbot controls, cannot causallyattribute swing. Combineddescriptive spread38.9pp,not independentpopulation estimate.

Report fresh-confirmation-study-20261005/Full_Manual_Inspection_2026-10-05.txt. Allfrozenhashes/finals/counts/baselineverified;all812projects158deficits inspected,focusedearlySwift/Mobilelosses andallMobiletails. Mean63.08median56,20within50–100;all9Mobilelosewith20–53Cyclecleanup tails. Route diversity preserved. Construction306/812active;2433/7386Supplyneveractive32.9%. Storm132starts14active,592neveractiveSupply. No voluntaryselfdeficits detected.

Recommendations NOTIMPLEMENTED: balancedopponent1–2meetings next36games,map4–5,retainseat/strategybalance. Savedbudgettestcandidates VoidExpand+4remote0S1MP,SwiftCreate6at1S1MP,Mobile70%intrinsic(full12=>8)withoutdefence/repairbuff;holdother9pendingevidence. Stormvaluationshouldtestpresenceatcompletioninsteadcurrentconcentration;no blanketconstructiondiscount/forcedcompletion. No newbatch,timer,publishingortraitedit. Separate manualmarker supersedesautomaticpending. RootbaselineandDessicasuspendedunchanged.

## 5 October 2026 — Fresh confirmation RUNNING

User requested continuation after usage interruption. All qualification completed before interruption; batch was NOT previously launched. Started12:05SydneyAEDT5October, wrapperPID16520. Directory fresh-confirmation-study-20261005. 36 NEW candidate-only games, one worker, no controls reused or run. Expected55–70minutes (13:00–13:15, allow until13:20). No timer, automation, automatic follow-on, publication or baseline promotion. Do not duplicate.

All12traits frozen at pursuit-parity candidate values (screening spread22.2pp). Fresh seeds/opponent groupings; eachtrait9appearances/3perseat/3trait-led plus each6generalstrategiesonce. 18template/18generated maps. Not a paired causal comparison;9appearances still limited evidence.

Bot-only changes construction_planning.py/construction_coverage.py: safe surplus terminal Scout host restoration, only funded positive-value plans; projected Scout effects use funded repaired hull/location and charge restoration resources/delay. Actual case24 orbital cannons veto solo interception even at full hull, so no claim tail solved. Cannon-free boundary fixture routes legal repair. Case17 replacementScout completed115 but same enemy elimination116 as existing queue; no forced procurement adopted. StormTransit sampled case26 completion unavailable at40 due reserve, negative value/emergency60; no rules changes. Preparation_Findings_2026-10-05.txt and saved evidence explain.

Qualification616regressions,77savedchoices,143historicalreplayedorders,114smokeorders,12pursuit-safety+9readinesschecks. Exact prior prefixes3469orders,10states. Twelve-Cycle saved suffixes244control/244candidate/239forced-procurement independently replayed. Initial added fixture failures fixed using valid ownership/hull cleanup, no engine relaxation. Baseline balance_sim.py remains56e855e9c23a88e8122696256b71bc6f2f38fa7137470de10f1903bc0208cffc; prior frozen studies and suspendedDessica unchanged.

On completion inspect manifest/results/completion-summary/full-inspection-evidence/full-inspection-summary; automatic POSTPROCESSING_COMPLETE is NOT manual verdict. Evaluate all12traits25pp observedspread,50–100Cycle pacing,shortages,construction delivery/waste,attackchoices,Mobile pursuit. No humanSoulstormwinrate inference. No further batch automatically.

## 5 October 2026 — Pursuit-parity full manual inspection COMPLETE: screening PASS

Report: pursuit-parity-study-20261004/Full_Manual_Inspection_2026-10-05.txt. All 36 new candidates and 36 saved controls resolved/replay-validated; 55,368 orders. Frozen hashes, all final snapshot hashes, paired initial conditions/settings and protected root balance_sim.py hash checked. Runtime55.12minutes; finished00:04Sydney. No active batch or automatic follow-on.

Trait spread33.3 ->22.2percentage points, PASSES creator25-point screening threshold. Fortification/Mobile/Void4/9; Siege/War/Efficient/Martial/Salvagers/Dread3/9; Industrial/Swift/Endurance2/9. Preserve all current trait numbers. Three winner changes all involve Fortification: loses12toDread and32toWar, gains22fromSwift. Its Muster0->13, meanMP48.7->32.7, cap observations4->0. Twenty-four paired order sequences identical. Nine appearances/trait; repeated screen, not independent confirmation. Seats balanced3each; strategy and trait-aware mode coverage not fully equal.

Pacing mean60.25,median53.5;20/36within50–100,14shorter,2longer. Pursuit cases16:106->87,24:109->107,17:158unchanged. Additional exact recorded prefix replay3730orders inspected8construction states. Case24 Scout host remains4/5 atCycles70/80/90, Build correctly illegal; funded restoration exists but project_fleet_order excludes Scout. At100 full-host reservation finally applies. Case17 has no live Scout at110; old project destroyed36, existing-project correction cannot trigger. Pre-fleet saved valuation gives new Scout positive scores; procurement queue comparison still needed, not a missing legal action.

Deficits129->135 entirely in Fortification-containing games; Mobile remains19. No detected voluntary self-deficit. Do not broadly boost income. Construction starts695->724, active285->292; never-active spend1897->2049 (28.9->30.3%). Storm Transit contributes96/152extra; more than half net extra never-active spending is projects still incomplete at ending. Keep rules fixed; inspect completion discipline rather than blanket discounts. Ground1050times chosen with naval legal; bombardment157times with ground legal. Route diversity remains.

Recommended, NOT IMPLEMENTED: (1) freeze trait numbers, (2) qualify Scout host restoration using normal safe travel/Expand and Scout-aware funding/value, not blindly adding it to MILITARY valuation, (3) compare new Scout versus existing queue in savedcase17, (4) targeted Storm Transit completion checks, (5) fresh balanced approximately-hour confirmation after qualified bot corrections, no repeated trait-tuning loop. This inspection starts no new game, timer, automation, publication or baseline promotion. Separate MANUAL_INSPECTION_COMPLETE.json supersedes automatic pending flag. Dessica remains suspended.
## 4 October 2026 — Pursuit-parity combined screen RUNNING

User authorized inspection recommendations. Launched23:09SydneyAEDT4October,wrapperPID22124;36newcandidate games versus36exactfinalist-parity controls,allpaired,nineappearances/trait,noholdout. One worker. Estimate45–60minutes,approximately23:55–00:10Sydney(5October after midnight). No timer,automation,follow-on batch,publishingorbaseline promotion. Do not duplicate launch.

Changes: Fortification free Defend4/Defended/+3Supply now+1Manpower(previous2). Other11traits unchanged. Bot correction for terminal Mobile pursuit: reserve at most one healthy safe surplus host of an existing unfinished Scout from ordinary chase movement; prioritize its completion when normal funding/safety checks pass and no defensive emergency. No forced purchase or extra action. Protect ordinary wars, insufficient spare strength, damaged/threatened hosts. Retain Mobile60%intrinsiccombat.

Qualification616regressions,14harnesschecks,12saved-state pursuit safety checks,77savedconstruction decisions,143historical replayed suffixorders,119smokeorders across12traits. Exact finalist pursuit prefixes3560orders reproduced. Paired12Cycle counterfactuals: control417/candidate293 independently replayed orders. Cases16/24 candidate eliminateMobile at86/85 fromCycle80;controls havezero battles through91. Case17 both resolve at116. Initial reservation-only variant retained; final completion priority solvescase16. DetailsPackage_Rationale_2026-10-04.txt. Local initial regression failures preserved; intendedtraitexpectations updated and redundantplanupdatebug corrected. Baselinebalance_sim SHA remains56e855e9c23a88e8122696256b71bc6f2f38fa7137470de10f1903bc0208cffc.

On completion inspect full12trait spread against25percentagepoints,50–100Cycle distribution,Mobile pursuit,FortificationMuster/Defend choice,shortages andconstructiondelivery. Counterfactual evidence is not campaign win-rate proof. Nine appearances/trait on reusedscreening scenarios; independentconfirmationaftertarget. Automaticpostprocessing is not manualinspection. Frozencontrols,rootbaseline andsuspendedDessica unchanged.
## 4 October 2026 — Finalist-parity full manual inspection COMPLETE

All 36 candidate games and 36 saved controls resolved/replay-validated, 55,699 recorded orders; frozen hashes and root balance_sim.py protected hash verified. Report: finalist-parity-study-20261004/Full_Manual_Inspection_2026-10-04.txt. Separate MANUAL_INSPECTION_COMPLETE.json supersedes automatic manual-pending flag without rewriting frozen evidence.

Spread improves 55.6 -> 33.3 percentage points, still FAILS 25-point requirement. Fortification5/9; Mobile and Void4/9; Siege, Efficient, Martial, Salvagers, Swift3/9; War, Industrial, Endurance, Dread2/9. Other eleven span22.2 points. Mobile gains cases2,3,34 against unchanged non-Fortification opponents; Fortification loses22 to Swift. Five winner changes,19 identical order pairs. Screening data reused; nine appearances per trait, no independent holdout.

Fortification stockpiling falls (MP-cap observations23->4), but only1 deficit and363 Defends,120 with zero restoration; no Muster used. Recommend NOT YET IMPLEMENTED +3Supply/+1Manpower free Defend, preserving4 restoration/Defended; qualify personnel choice before next screen. Hold Mobile60% intrinsic combat and other10 traits.

Mean59.69Cycles,median53;17/36 within50–100,16 shorter,3 longer. Long cases16/17/24 finish106/158/109 with Mobile surviving79/78/69Cycles after its last stationary holding. Cases16/24 have34/37 consecutive battle-free Cycles. Qualify legal pursuit alternatives from saved states before any bot correction; do not nerf Mobile combat or invent elimination timer to hide cleanup. Deficits115->129; Mobile's largest rises14/17 involve attacks/events and no recent construction spending. Construction activation42.0->41.0%, never-active spend share27.4->28.9%; no blanket construction buff justified.

Next, only after authorization: bounded Fortification and saved pursuit checks, then one complete approximately-hour combined screen if qualified; independent confirmation after target. No new batch, timer, publication or baseline promotion launched. Dessica remains suspended.
## 4 October 2026 — Two-outlier finalist-parity RUNNING

Authorizedtwoadjustments implementedin finalist-parity-study-20261004. Started21:27SydneyAEDT,wrapperPID20388.36newgames/36exactroster-paritycontrols,allpaired,nineappearances/trait,noholdout. Oneworker,estimated45–60minutes,finish22:15–22:30Sydney. No timer,automaticfollow-on,publishingorbaselinepromotion.

FortificationDefendMP3->2,retainfree4restore/+3Supply/Defended. Mobileintrinsiccombatnearestwhole60%,(3*hull+2)//5;full12=>7;constructionaddedhullnormal. Other10traitsunchanged. Necessarybotupdate:compareMuster3MPvsDefend2MP+3Supply;chooseMusterwhenMPbelowreserveandSupplymeetsreserve,subjecttoexistingemergencydefencepriorities. Onlyshared_sim.py/operational_bots.py changed in engine. DetailsPackage_Rationale_2026-10-04.txtandfingerprintedRecovery_Parity_Rulesoverrides.

Qualification611regressions,13focusedchecks,14harnesschecks,77saveddecisions,143historical+103latestreplayedcontinuationorders,119smokeorderscoverall12traits. Baselinehashverified. Controlsreusedwithexactfingerprints. Prior frozenstudiesandDessicaunchanged. No duplicate launch. Oncompletioninspectfullroster25ppspread,FortificationDefend/MusterchoiceandMP,Mobilecombat/pursuit,50–100Cyclepacing,resourceexposure,constructiondelivery. Automaticpostprocessingisnotmanualinspection. Ifscreenpassesrecommendfreshindependentconfirmation,nothumanSoulstormwinrateclaims.

## 4 October 2026 — Roster-parity inspection COMPLETE

36newgames/36controls,54,542traceorders,allresolved/replayvalidated;53.52minutes. Fullreport roster-parity-study-20261004/Full_Manual_Inspection_2026-10-04.txt. Spreadstill55.6pp,FAIL25pp,buttenothertraitsnow22.2–44.4%. Fortification6/9,Mobile1/9outliers. FortificationMPmean17.3->61.1,deficits15->1;MobilelosesfourwinsagainstnonFortificationopponents,ground306->179,moves553->857. Constructionactivation39.5->42%,neveractivecostshare34.2->27.4%;shortageexposureimproves. Mean61.58Cycles,22within50–100,2longMobilegames107/123. SuggestedNOTIMPLEMENTED:FortificationDefendMP3->2(keep3Supply/free4restore),Mobileintrinsic60%roundednearest(full12=>7),holdother10. Bot mustcompareMuster3vsDefend2MPafterchange,notassumeDefenddominates. Qualifycost/invariants,thenonepairedscreenifapproved;independentconfirmationaftertarget. No newbatch,timer,publishingorbaselinepromotion;Dessicapreserved.

## 4 October 2026 — Combined roster-parity comparison RUNNING

User authorized proceeding with full inspection recommendations. Study roster-parity-study-20261004; start19:11:59SydneyAEDT,wrapperPID13992.36newgames versus36exact decision-parity controls,allpaired,nineappearances/trait,noholdout. One worker;estimated45–60minutes,approximately20:00–20:15Sydney. No timer,automation,automaticfollow-on,publicationorbaselinepromotion.

Nine-trait provisional package:War12Supply/Logistics;Martial4MP;Swift6/6Create2S2MP,halfupkeep,normalExpand;Mobileintrinsiccombatceil(hull/2),normaladdedconstructionstrength,12hull/noMobileupkeep unchanged;Dread1+max(1,ceil(committedstrength/5))eachresource;FortificationfreeDefend4plus3S3MP;Industrialdiscount3minimum1,initial2normalcontinuation/Repair;VoidordinaryExpand4for0S0MP,yardindependent,oldzeroS/halfMPupkeep;Salvagers3win1lossdraw,capture1,no uncontestedreward. Efficient7,Siege,Endurance held. Bot awareness updated for creation/expansion costs and FortificationDefend now dominating ordinaryMuster. Detailed arithmetic and exploit considerations in Package_Rationale_2026-10-04.txt. Rules overrides in candidate/Recovery_Parity_Rules_2026-10-04.txt are replay-fingerprinted.

Qualification611regressions,9additionalfleet/taxedges,14harnesschecks,77saveddecisions,145historical+106latestreplayedcontinuationorders,119smokeorders across12traits. Original prefix snapshots reused, not freshly re-reproduced. Legacyexpectation failures preserved and explained in Qualification_Notes.txt; final checks passed. VALIDATION_PASSED.json protects baseline hash. Old copied freeze_decision_package.py is prior-study preparation logic, not the new qualification record; do not run it. Study already prepared/frozen/launched, do not duplicate.

On completion inspect all12traits against25ppspread;50–100Cyclepacing,resourceexposure/caps,FortificationhealthyDefendrewards/MPattrition,Voidfreerefituse/actionlocks,SwiftCreateeconomy,IndustrialMajoractivation/rebuildloops,SalvageWingstacking,Dreadsurcharge,Mobilepursuit andcapacity. No claim of humanSoulstormwinrate. Preserve frozen data,rootbaseline,suspendedDessicaCycle21. Completion postprocessing is not a manual verdict.

## 4 October 2026 — Decision-parity inspection COMPLETE

Report: decision-parity-study-20261004/Full_Manual_Inspection_2026-10-04.txt. All72traces/53,236orders checked, hashes and baseline verified. 27/36 identical order sequences; nine divergent games; zero winner changes. First divergence construction5/fleet3/faction1. Spread remains55.6pp, fails25pp. Pacing mean60.89,24/36in50–100. Pursuit mixed:case16improves124->103,14worsens79->99,34worsens78->89. Case35improvement starts at construction, not isolated pursuit proof. Fortificationcase11Musterfirstdifference removes2deficits but still loses earlier. Construction activation39.0->39.5%,neveractive spend share worsens33.7->34.2%; no broad delivery fix. Next recommendation: combined trait-side package after bounded cost/decision checks, not another broad bot-only cycle. Candidate directions in report, no numerical changes implemented or batch launched. Separate manual marker supersedes automatic pending flag. Preserve frozen data, baseline and Dessica.

## 4 October 2026 — Decision-parity comparison launched

User authorized inspection recommendations. decision-parity-study-20261004 started16:08SydneyAEDT; wrapperPID10356. 36newgames/36exactrecovery-paritycontrols,allpaired,nineappearances/trait,noholdout. One worker;estimate50–60minutes,around17:00–17:10Sydney. No timer/automation/publication/follow-on. Traits and resolver unchanged; only operational_bots.py and construction_planning.py changed, with provenance text in candidate Recovery_Parity_Rules.

Corrections: prioritize legal Scout Mobile interception before assembly; distinguish stay+Expand recovery from evading recovery; retain main pursuit group and stage surplus at legal escape destinations with donor protection. Multi-action construction rejects presently exposed hosts; immediate final Build remains eligible. Scarce Manpower can precede discretionary host maintenance when Supply reserve is met, but imminent holding loss retains defence priority. These are bounded heuristics, not proven fixes or changes to game rules.

Qualification:600regressions,14harnesschecks,77saveddecisions,143historical+103latestreplayedcontinuationorders,119smokeorders across12traits;2725originalprefixorders independently reproduced for case16C80P0,35C80P1,13C80P1. Actual Fortification case13 still Defends its endangered capital, appropriately; do not claim deficit issue solved. Failure history preserved in Qualification_Notes.txt and first-run logs; latest harness canonical group-order check corrected, engine unchanged. Baseline hash verified.

On completion inspect all36paired results, trait spread25pp,50–100Cycle distribution, Mobile pursuit tails, construction activation/never-active spending, Fortification manpower trajectory and routes. Check automated completion does not imply manual inspection. Do not launch another batch automatically. Preserve all frozen sources, root baseline and DessicaCycle21.

## 4 October 2026 — Recovery-parity manual inspection complete

36 candidate +36 exact controls;52,611 traced orders. Report: recovery-parity-study-20261004/Full_Manual_Inspection_2026-10-04.txt; separate MANUAL_INSPECTION_COMPLETE.json supersedes automatic manual-pending status. Spread44.4->55.6pp fails25pp; Fortification0/9, four leaders5/9. Mean61.75Cycles;22/36 within50–100; all resolved. Construction activation essentially unchanged39%; shortage exposure improves overall. Pursuit case16 worsens103->124Cycles. Fortification late Defends genuinely repair capitals; do not claim proven wasted-action loop. Recommendations are diagnostic/correction priorities, not implemented numerical changes. No new batch, timers, publication or baseline promotion. Frozen evidence and Dessica preserved.

## 4 October 2026 — Recovery-parity combined package running

User approved full inspection recommendations. Isolated directory recovery-parity-study-20261004. Started 2026-10-04T14:17:24.2986055+11:00;wrapperPID22848. One worker,36newgames against36exactforce-paritycontrols,allpaired. Estimated50–60minutes;approximately15:10–15:20SydneyAEDT. No timer,monitor,automaticfollow-on,publicationorbaselinepromotion.

ImplementedWar9Supply/Martial5MPperLogistics;Efficient7Reinforce/Muster;SwiftCreate6/6at1S1MP,halfupkeep,normalExpand;Siegevictoryextra1instead2. Other7traits held. Swiftbasecapacityrecordedseparately:merge transfersconstructioncapacity but cannot launder Swift's extra base point into an ordinary survivor. Existing fleets not retroactively upgraded. FullweightedconstructionSupplycostreplaces0.65acrossvaluationpaths. Pursuit accounts for visible jointlyaffordableDefend/Expand recovery and callsinlegalreinforcements before repeating a repairableattack. Existing legalScoutinterception/surplusretention guards retained;no omniscientinterception,newmovementruleorforcedcapitalsurrender. No guarantee allpursuittailsresolved.

Qualification592regressions,27focused/edgechecks,7finalvaluationchecks,14harnesschecks,77savedsituations,143replayedcontinuationorders,119smokeorderscoveringall12traits. Originalpursuitprefixes independentlyreproduced1053and861orders;case34nowselectsreinforcementmovement. BothForgecounterexamplesstillchooseForgeatfullcost. Intentionalhistoricaltestexpectationchangesrecorded;originalfailuresretained. Acceptedbaselinehashverifiedunchanged.

Aftercompletionreadmanifest/results/completion-summary/full-inspection-summary/paired-trait-outcomes. Automaticpostprocessingdoesnotconstitutefullmanualverdict. Evaluateall12traits,25ppspread,50–100Cyclepacing,constructionwaste/activation,resourceexposure,threeattackroutes,andMobilepursuitcases. Controlsall36,NOunpairedfreshcases. Nineappearances/traitisscreening,notpopulationcertificationorhumanSoulstormwin-rateprediction. PreserveDessicaCycle21andallpreviousfrozensources.

## 4 October 2026 — Force-parity inspection complete

All36newgames and36controls inspected. Spread44.4pp misses25pp. Full recommendations and evidence: force-parity-study-20261004/Inspection_Recommendations_2026-10-04.txt and next-package-inspection.json. Proposed NOT IMPLEMENTED: War9,Martial5,Efficient7,SwiftCreate6/6at1S1MP(normalExpand/halfupkeep),Siegevictorybonus1instead2;holdother7. Full-cost construction scoring and repair-aware Mobile pursuit. Three long games involved Mobile pursuit; case34 used3of8fleets repeatedly. No new batch, automation or publication. Preserve baseline/Dessica. Actual design36allpaired, no freshholdout; frozen old explanatory prose is stale.

## 4 October 2026 — Force-parity package running locally

User approved implementation and a new complete batch. Directory: force-parity-study-20261004. Started 2026-10-04T12:53:13.5103758+11:00; wrapper PID 19472. One worker, 36 new games and 36 exact-source saved completion-study controls, all36 paired. Expected45–60minutes from launch, approximately13:40–13:55Sydney AEDT. No timer, monitoring automation, automatic follow-on or publication. Preserve accepted baseline and suspended DessicaCycle21.

Implemented Mobile intrinsic combat contribution ceil(2*intrinsic current hull/3), normal added fleet-construction strength; Endurance restoration2 and half both upkeep resources; Void half Manpower upkeep retaining prior benefits; Dread tax1+2*ceil(declared engagement Strength/5)of each resource before losses, ground bonuses included. Other eight traits unchanged. Removed duplicated construction completion-delay divisor; retained reserve/legal completion and independent-alternative checks. Mobile added hull absorbs damage first; intrinsic conversion cannot create repair capacity.

Qualification:592 regressions,15 focused/edge checks,14 harness checks,77 legal saved choices,143 independently replayed continuation orders, five short smoke cases covering all12traits. Both inspected economic counterexamples now select Forge. Known Bay remains legal but does not receive forced sunk-cost priority. Initial historical-expectation failures retained in regression-first.txt and intentional updates recorded. Source control fingerprints matched retained completed candidate exactly.

On completion inspect results.json, completion-summary.json, full-inspection-summary.json and paired-trait-outcomes.json; POSTPROCESSING_COMPLETE.json still requires manual verdict. Evaluate all12traits against25pp observed spread,50–100Cycle pacing, routes, shortages and construction activation. No human Soulstorm win-rate inference. Small screening sample: nine appearances per trait.

Reporting caveat: copied reuse console text mentions12fresh cases and the copied summary limitations string mentions old24/12split. Those prose strings are stale; manifest and cohort aggregation contain36 controls and36 candidate, all paired, no fresh cases. Do not repeat the stale strings. Frozen evidence must not be edited during run; correct explanatory reporting after completion. Active-duration inspector now uses actual cycle_close tag.

## 4 October 2026 — completion-delivery FULL MANUAL INSPECTION COMPLETE

Read completion-trait-study-20261004/Full_Manual_Inspection_2026-10-04.txt and MANUAL_INSPECTION_COMPLETE.json. All60traces/41,246orders/180factionappearances/1,161projects/260deficits inspected;240protectedhashes.2,951Logistics arithmetic checks,7,200player setups. Additional4,683exact prefix replay orders reproduce189construction and102Faction choices across12cases. Isolated no-tempo-division same-state diagnostic changes19construction choices;not campaign outcomes. Old POSTPROCESSING manualpending superseded by separate completed record. No new batch,engine/rulechanges,timer or publication.

Verdict:NOT within25pp. Paired spread83.3->66.7pp; overall36cases also66.7pp. Nine appearances each:Mobile6,War/Salvagers5,Efficient4,Siege/Swift/Fortification3,Industrial/Martial/Dread2,Void1,Endurance0. Nevercompare36aggregatewith24controls aspaired. FreshIndustrial2/3vs0/6paired,Swift0/3vs3/6paired;uncertainty/matchups matter. Tenpairedwinnerschanged with traitnumbersunchanged. All36resolved26-87Cycles,mean53.17,20within50-100and16shorter.

Keep reserve/independentqueue correction, revise blanketvalue/completiondelay. Pairedactivation177/488(36.3%)->188/463(40.6%),neveractivespending1565->1275,total4508->3908;startswithunfinished300->240. BUT0Forge/Academystarts versus5/4controls. Exactcase0C3IndustrialDepotraw14.7vsForge26.0 becomes7.35vs6.5afterdivision; removingonlydivisionselectsForge. Factor double-penalises timing already represented in returns. ExistingBayactualcase11activatesC3ratherthandyingunfinished.13SystemDefence/9SystemRepairneveractivate;StormTransit15/120. No blanket catalogue discount from unpopularity.

Report defect corrected separately:original inspector uses nonexistentcycle_close_after;active_observed_cycles fields unusable. Independent exposure-and-trait-inspection.json usesactualcycle_close. Wins,activationdates,spend/results unaffected;frozen files preserved.

Supplypairedexposure126/3714->163/3513(3.39->4.64%);MP130->122.102triggersvs99;zero self-order. Biggestincreasesfollowenemyattack/warfare/Defend andcapitalreplacement+overlappingrationing,notrecentconstruction. Only12triggerswithin3Cyclesconstructionvs25control. Knowncompulsory-upkeep/defence-reserve warfare choices warrantattention,notglobalincomebufforundoingdeficits. Routesused:paired1601ground,148naval,200bombard,57structure;716groundchoicesfrom830menusalsocontainingnaval. Notidentical-target orhumanoddsproof. Siege9defeatcapturesall36.

NEXT COORDINATED RECOMMENDATION ONLY, UNIMPLEMENTED/UNAPPROVED: constructionnetvalueoverfixedhorizonwithactualactivation/delay/risk,removeblanketdivision; preserve reserve/queue fixes. Mobileintrinsiccombatstrengthceil(2*currentDefence/3),full12defence->8Strength;keep12holdingdefence,shipyard,income,noupkeep,normalfleetupgradebonuses(distinguishintrinsic/bonusduringqualification). Endurancerestore2andhalveSupplyupkeepaswellasMP. VoidhalveMPupkeepretainingexistingremote+4Expand0S/1MPandzeroSupkeep. Dreadtax1+2*ceil(committedengagementStrength/5)ofbothresourcesinsteadassetcount;declarebeforeinit/cannoncosts,qualifyallies/groundbonusandMobileconversion. Holdother8traits(War7,Martial6,Efficient6,Salvagers2/1+capture1,Swiftcurrent,Siegecurrent,Fortification4free+3S,Industrialcurrent). Arithmeticonly:Enduranceextra129restored/153Supplysaved,Void191MPsavedonsavedstates;notnewoutcomes. Do notautomaticallylaunchorclaimonebatchguaranteesparity. AIresultnotSoulstormhumanwinrate. BaselineandDessicaunchanged.

## 4 October 2026 — construction-delivery screen RUNNING, traits unchanged

User authorised the manual-inspection recommendations. Study: completion-trait-study-20261004. Started10:51Sydney AEDT on4October, wrapperPID19696; one worker.36NEW games plus24 exact saved coordinated controls. Estimate45–60minutes, approximately11:36–11:51Sydney. No timers, reminders, staging or automatic follow-on. Do not duplicate. Read manifest.status/new_games_completed,progress.txt,wrapper-errors.txt,batch-error.txt and launch.json. completed includes24reused controls, NOT24new games.

Only live engine changes: construction_planning.py and operational_bots.py. Trait rules identical to coordinated package (War7,Martial6,Voidremote,Fortification3Supplygrant,other8unchanged). Legal ready finalBuild may pass below soft preferred reserve, preserving positive resources and compulsory threat/upkeep funding; no deficit, restoration or queued-cost exception. Standalone alternatives evaluated independently of existing queue; explicitly retained sequences include real predecessor costs/delays. Positive value divided by completion delay for consistent delivery-tempo comparison; negative values not diluted. This heuristic may favour short projects, so inspect Major construction viability. No forced sunk-cost completion or exposed-host bypass.

Qualification:592regressions,6edgechecks,14harnesschecks,77saved decisions,4three-Cycle diagnostic suffixes/145independently replayed orders,5two-Cycle smoke cases/119verified orders coveringall12traits. Original failed regression log retained; one test intentionally updated because historical discretionary MP spending cannot veto an immediate Supply-only effect. Restoration-cost exception was tightened to preserve existing guard. Same savedcase11IndustrialCycle4 now completesBay; originalCycle5 funding passes but separate exposed-host tactical veto remains. No claim counterfactual proves a campaign win.

Schedule:24pairedcases and12freshUNPAIRED;9appearancespertrait,3perseat,all66opponentpairs,18matched/18generatedmaps. Eachtrait4/5map-familyappearances. Schedule optimisation uses coverage only,nooutcomes. Report control24 against candidate_paired24 ONLY. candidate36overall and fresh12 have separate denominators. Never call36vs24 paired.25pp observedspread directional, not certification; one win11.11ppoverall. Largerfreshconfirmation onlyafterpromisingresults.

Inputs/harness frozen;everygame independently replays beforecounting.200Cyclehorizon;unresolvedsurvivorsnotwins. Keepalloutliers,stoponactualfailure,preserveevidence. Wrapper runs summary,all60traceinspection,24pairedcomparisonthenwritesPOSTPROCESSING_COMPLETE manual_verdict_pendingtrue. Manualreview must inspectall12traits,pacing,resourcecauses,constructionactivation/loss/spend,MajorversusMinor,bothpaired/fresh cohorts,attackroutes. AI results donotpredict humanSoulstormwinrates. Study_Plan.txt and VALIDATION_PASSED.json have details. Baseline,prior evidence and suspendedDessicaCycle21unchanged;noexternalpublication.

## 4 October 2026 — coordinated package FULL MANUAL INSPECTION COMPLETE

Read coordinated-trait-study-20261004/Full_Manual_Inspection_2026-10-04.txt and MANUAL_INSPECTION_COMPLETE.json. All48traces/34,709orders/144factionappearances/885projects/204deficitentries inspected;236protected hashes checked in full audit.2,460Logistics observations and7,200deterministic player-setup checks. Additional1,934exact prefix replay orders;77actual pre-selection decisions reproduced exactly, eleven traits; old-queue-only same-state counterfactual changes6choices, not new campaign outcomes. Engine/rules unchanged.

CRITICAL TEST-DESIGN FINDING: six appearances each and24single-winner games means observed spread<=25pp REQUIRES ALL12traits to win exactly2. One win=16.67pp; average2wins, so any deviation creates at least33.33pp spread. Do not use this small-screen raw spread as parity certification. Exact equal-strength independent1/3 scheduled-winner lottery yields probability9.85149441049e-6of that perfect tie (~onein100,000); mathematical null illustration, NOT evidence actual game is balanced. Current schedule covers48of66trait pairs (24twice/24once), eighteen absent. Same-case repeated tuning risks fitting specific opponents. The creator's25pp target remains; the measurement must improve.

Observed spread remains83.33pp, unchanged from prior package; it rose66.67to83.33in preceding package. New wins/6:Mobile5,Swift4,Siege3,Efficient/Martial/Salvagers/Dread2,War/Void/Endurance/Fortification1,Industrial0.14of24winners changed. Mobile gained two games from War and one from Industrial; do not attribute its whole swing to a direct Mobile buff (unchanged in this package). Historical versions must not be pooled or unresolved survivors treated as losses.

DOCUMENTED PLANNER SETBACK: starts397→488,ever-active173→177(43.6→36.3%),spending on never-active work30.0→34.7%;starts alongside unfinished work174→300. Queue storage works, but newly selected schedules can displace immediate completion and then fail reserve reevaluation. Case11IndustrialCycle4:14S/20MP,fullhost,Bay2/3. New bot startsAssaultCruiser; oldqueue-only chooses1SupplyBaycompletion. Cycle5has12Supply but desiredreserve16(previous7), so allBuilds rejected even1Supply immediate completion; host full. Bay/Cruiser bothdestroyedCycle6inactive. This isolates decision effect, not proof entire campaign would reverse. Original qualification proved legality, not sustained delivery. Target immediate-completion versus soft-reserve rules and realistic multistage commitment, preserving strict positive-resource legality; do not force sunk-cost completion.

Useful gains:VoidExpands45→178,captures39→83;SystemRepair speculative starts28→7. But noneof7activated. Twelve unused profiles; other economic constructions andCannonsdeliverwell. Industrialownactivation22/41→12/30,spend221→147:cannotblameoverspendingalone. Pacingmean59.17,median54,range30–131;14within50–100,9short,1long;allresolved. Supplyexposure3.39%,Manpower3.50%,99triggers,zero self-action triggers. Ground1668/naval189/bombard209/targeted50;allroutesused. GlobalSoulstormdifficultyissue remainsdeferred;AI outcomes arenothumanwinrates.

RECOMMENDED, UNIMPLEMENTED: holdcurrenttraitnumbers(War7,Martial6,Voidremote,Fortification3grant,other8) while qualifying documentedconstructionexecution correction against consecutive saved situations. Mobile/Swiftremainupper-tierwatchitems;Industrialdeliveryneedsrepair. Use acomplete36-gamescreen(nineappearances/trait,2–4wins=22.22pp) withfreshcases andimprovedopponentcoverage, labelledpaired/unpaired correctly; do notcompare36aggregateaspairedwith24. Estimated45–60minutesfromobservedthroughput,notguaranteed. Still directional;largerfreshconfirmationafterpromisingresults. No new batch/patch/timer/publication/baselinepromotionduringinspection. Userapprovalneededbeforelaunchingnextwork. HistoricalPOSTPROCESSINGmanualpendingissupersededonlybynewcompletionrecord. AcceptedbaselineandDessicaunchanged.

## 4 October 2026 — coordinated screen COMPLETE; full manual inspection pending

coordinated-trait-study-20261004 finished all24new games, independently replay-validating17,071new orders, with24exact saved controls (34,709orders total). No failures. Automatic summary,48-trace inspection and paired outcomes completed09:35:47Sydney AEDT, approximately30minutes after launch. No Python runners remained at10:06status check. Do not restart or launch another batch automatically. POSTPROCESSING_COMPLETE.json explicitly leaves manual_verdict_pending=true.

Initial aggregate findings only: six appearances each; Mobile5wins,Swift4,Siege3,Efficient/Martial/Salvagers/Dread2each,War/Void/Endurance/Fortification1each,Industrial0. Observed spread83.33pp remains above25pp target; leadership shifted rather than parity achieved. All games resolved,mean59.17Cycles,median54;14within50–100,9below,1above. Supply-deficit exposure4.78%→3.39%;Manpower3.83%→3.50%. These are combined-package screening results, not isolated causal estimates, precise trait probabilities or human Soulstorm predictions. Need inspect changed wins, Mobile/Swift dominance, Industrial construction decisions, actual queue retention, repair alternatives, shortages and routes before prescribing further edits. Automatic evidence covers885project starts and204deficit entries acrossbotharms.

No new batch, code/rule changes, timer, publication or baseline promotion. Accepted baseline and suspended Dessica unchanged. See completion-summary.json,full-inspection-summary.json,full-inspection-evidence.json andpaired-trait-outcomes.json. The earlier full inspection belongs to the previous creator-trait study, not this newly completed screen.

## 4 October 2026 — coordinated trait and planning comparison RUNNING

User approved the full inspection recommendations. Work directory: coordinated-trait-study-20261004. Started 2026-10-04T09:05:53.5656179+11:00; wrapper PID 18652, study PID 21440. One worker, 24 NEW candidate campaigns plus24 exact saved creator-trait-study-20261003 candidate controls. Same balanced schedule: six appearances pertrait, twice perseat;12matched/12generated. Estimated40–60minutes from launch, approximately09:45–10:05Sydney (AEDT) on4October. This is one complete screen, not staged or followed automatically by another batch. Do not duplicate the runner.

Approved and implemented: War Economy +7Supply/Logistics; Martial Culture +6Manpower/Logistics; Void ordinary Expand without shipyard (+4,0S/1MP,capacity/action/positive-resource rules); Fortification free Defend restores exactly4 and grants3Supply. Hold other8traits. Read candidate/Coordinated_Rules_2026-10-04.txt; this overrides four entries in the historical creator trait reference. No accepted-baseline promotion or changes to suspended DessicaCycle21.

Bot corrections: persist chosen finite construction sequence in replayable bot memory, revalue each Cycle, prune completed/destroyed/captured work; do not automatically queue all remembered projects. Repair demand compares real local or safe round-trip yard refits using shared budgets and future Fleet Actions. Invalid captured objectives do not justify imaginary redeployment. Existing phase-by-phase objective refresh retained. All modifications are isolated from old evidence and controls.

Qualification:582regressiontests(14new focused checks included),12harness checks,6edge checks.70usable saved Fleet/construction positions across all12traits;1512original prefix orders replayed exactly. All70revised choices legally resolved with no resource/asset mutations from selection. Five two-Cycle synthetic smoke cases,119orders independently replayed. These are mechanics checks, not new balance campaigns.435source/control/baseline hashes checked. Initial failing output and intentional rule expectation changes retained. Saved case6Cycle10 rejects the old speculative SystemRepair purchase;Cycle20 chooses remote Void expansion rather than None.

Both engines and harness frozen before launch;24saved controls retained with provenance. Read manifest.new_games_completed, progress.txt, wrapper-errors.txt and batch-error.txt if present. Each new game must independently replay before it counts. All-game horizon200Cycles; unresolved survivors are not wins. Stop on failure, preserve evidence. Runtime estimate never permits silently dropping difficult games. Wrapper runs summarise.py,inspect_full.py,paired_outcomes.py and exits with POSTPROCESSING_COMPLETE.json manual_verdict_pending=true. A later full interpretation must cover trait25pp tolerance,50–100Cycle pacing, construction activation/loss/value, shortages, routes and revised trait/bot usage; no human Soulstorm win-rate inference.

No timers, reminders, automatic follow-ups, external publication or automatic next batch. No need for internet while the local process runs, but the PC must remain on. Prior inspection remains at creator-trait-study-20261003/Full_Balance_Inspection_2026-10-04.txt. Current implementation and qualification: Implementation_Summary_2026-10-04.txt and IMPLEMENTATION_COMPLETE.json.

## 4 October 2026 — creator trait FULL INSPECTION COMPLETE

Read creator-trait-study-20261003/Full_Balance_Inspection_2026-10-04.txt and MANUAL_INSPECTION_COMPLETE.json. All 48 saved traces / 39,306 orders / 144 faction appearances inspected; 230 protected input/reference/baseline hashes verified again. Additional saved-prefix replay checks: 2,614 general construction, 1,309 actual-purchase, 6,256 operational (overlap; not additional independent campaigns). 23 construction positions/501 assessments, 15 actual purchases/583 assessments, 143 operational positions and 7,200 deterministic player setup checks. Actual effective bot policies and economic fallback used. Historical POSTPROCESSING_COMPLETE.json manual-pending flag is superseded by this separate completion record.

Verdict: NOT within 25pp trait tolerance. Six appearances each: Martial 5 wins, War 4, Swift 3; Siege/Efficient/Mobile/Endurance 2; Industrial/Salvagers/Dread/Fortification 1; Void 0. Spread 83.33pp versus 66.67pp in these exact controls. Two old unresolved games are not losses; all 24 new games resolved, mean 56.79 Cycles, 15 within 50–100 and 9 shorter. All routes used; no human Soulstorm win-rate inference.

Martial made zero Muster actions, won 249/254 selected ground assaults, and held mean 61.83 Manpower at Cycle20 versus 30.6 previously (survivors only). Dread correctly charged 485 of EACH resource in 103 engagements. Void expansion benefits worked, but saved remote damaged fleets lacked legal refits. Industrial own activation improved 23/46 to 22/41 despite fewer wins: do not diagnose a completion collapse from win count. Fortification restored 245 defence on candidate positions versus 282 under preceding restoration amounts.

Construction activation overall 43.6%; 30.0% of construction spending went to never-active projects; thirteen profiles unpurchased. System Repair 2/28 activated; Storm Transit 8/65. Actual sampled purchases score positively under the effective policies, so no bogus claim of negative-score purchase fallback. Repair demand under-compares remote ordinary fleet refit journeys; forecasts can credit damage on fleets that redeploy before construction completion. Finite alternative construction sequences are evaluated but not persisted as the actual future queue. Correct these specific planning issues, not all rules or every unused construction price.

Supply deficit exposure 4.78%, Manpower 3.83%, but 105 triggers versus 107 old: shorter denominators and duration matter. New causes: 87 enemy orders, 14 events, 4 Logistics; zero self-action triggers. Recent construction preceding 20 entries is proximity, not proven cause.

UNIMPLEMENTED coordinated recommendation: War Economy +7 Supply per Logistics; Martial Culture +6 Manpower; Void existing ordinary Expand allowed without a yard (+4, 0S/1MP, capacity/action/positive-resource constraints retained); Fortification keep exact free 4-defence Defend, increase its Supply grant 2 to 3. Hold remaining eight traits, including Mobile no upkeep, Swift creation/half upkeep, Dread dual tax, Siege, Industrial normal subsequent progress and Salvagers current payouts. Couple with realistic repair/deployment/objective forecasts and a persisted, explicitly revisable construction sequence. Qualify against saved situations before any authorised new short roster screen. Values are proposed hypotheses, not approved changes or predicted parity.

No new campaigns, timers, publication, rule/bot edits or baseline promotion during inspection. Suspended Dessica and frozen evidence unchanged. The global Soulstorm difficulty issue and older pursuit/Scout limitations remain; resolved tails here do not prove their code fixed.

## 4 October 2026 — creator trait screen COMPLETE; initial results reviewed

creator-trait-study-20261003 completed all24new games and24saved paired controls without failures.17,638new orders independently replay-validated;39,306orders across both arms. Automated full-trace inspection covered48traces,844projects and212deficit entries. Finished00:13Sydney, approximately31minutes after launch. No new batch started. POSTPROCESSING_COMPLETE.json remains manual_verdict_pending=true: aggregate review is not the full causal decision audit.

Same24-case comparison: trait spread worsened66.67pp to83.33pp, above25pp target. Six appearances each: Martial5wins,War Economy4,Swift3,Siege/Efficient/Mobile/Endurance2each,Industrial/Salvagers/Dread/Fortification1each,Void0. Prior corresponding wins: Martial2,War1,Swift4,Siege2,Efficient2,Mobile0,Endurance2,Industrial3,Salvagers3,Dread0,Fortification3,Void0. Two old campaigns were unresolved; all new games resolved. Do not compare this directly to the earlier36-case44.4pp spread or call unresolved old survivors losses. One win here is16.67pp; the package comparison does not isolate each trait change.

Pacing improved: candidate mean56.79Cycles,median57,range27–90;15/24within50–100,9below50,noneover100/unresolved. Prior24case mean72.58including200Cycle unresolved cases, resolved-only mean61. Shortage exposure Supply4.39%to4.78%,Manpower2.75%to3.83%;zero self-action deficit triggers. Construction ever-active210/447(47.0%)to173/397(43.6%);spending on never-active projects1222/4874(25.1%)to1171/3904(30.0%). All routes remain used: candidate1737ground(including17Mobile),138naval,206bombardment,36targeted structures. Counts alone are not proof of route parity.

Initial judgement: pacing is promising but trait parity is not achieved. +10income traits are prime overshoot suspects; inspect matched outcomes and resource/combat histories before prescribing exact replacements. Also inspect weaker Industrial/Fortification/Salvager outcomes and Void's repeated0/6 to distinguish package interaction from bot usage. No automatic reversion or unapproved new trait values. Candidate mechanics qualified; baseline and suspended Dessica unchanged.

## 3 October 2026 — creator trait package one-hour comparison RUNNING

User requested approximately one hour of balance work on the implemented trait package. Single finite24-case comparison launched 2026-10-03T23:42:18.3083179+10:00; wrapper PID 11828, study PID 4256. Directory creator-trait-study-20261003.24NEW campaigns plus24 exact saved recovered-package candidate controls; six appearances per trait, twice per seat,12matched/12generated maps. No staged follow-on. Estimated50–60minutes from launch, roughly00:32–00:42Sydney on4October, based on approximately48minutes for these previous cases. New rules may change duration; an ETA is not permission to drop difficult games or mislabel a partial sample complete.

Candidate is copied exactly from creator-trait-revision-20261003/candidate, including the creator-confirmed Fortification4Defend and Swift half upkeep.568regression tests passed again in43.587seconds;12harness checks pass. Both engines, schedule and analysis harness frozen. Controls reused from completed evidence rather than rerun. All new orders independently replay before a game counts. First worker confirmed running with zero failures; do not duplicate.

Read manifest.json (new_games_completed, not completed which includes24controls), progress.txt, launch.json and wrapper-errors.txt. Wrapper runs summarise.py, inspect_full.py and paired_outcomes.py only after all24new games verify, then writes POSTPROCESSING_COMPLETE.json with manual_verdict_pending=true and exits. Manual review must cover all12traits/25pp maximum spread,50–100Cycle target, shortages/causes, attack routes, construction delivery and changed Dread/Salvagers mechanics. Six appearances means16.67pp per win; unresolved survivors are not wins; no human Soulstorm win-rate inference. Existing pursuit/Scout/project-schedule limitations remain and must inform interpretation.

No automation, notifications, publication, accepted-baseline promotion or change to suspended DessicaCycle21. Original rules/evidence untouched. The earlier implementation completion note means code qualification only; this newer entry records the balance run now underway.

## 3 October 2026 — creator-directed trait revision implemented and checked; NO NEW BATCH

Latest working trait candidate: creator-trait-revision-20261003/candidate, copied from recovered-package-study-20261003/candidate. Read candidate/Creator_Trait_Rules_2026-10-03.txt for the full twelve-trait reference; it overrides historical copied trait text and is pinned in replay inputs. IMPLEMENTATION_COMPLETE.json records modified file hashes. This is separate from the accepted baseline, not a promotion or balance sign-off.

User-directed changes: Mobile Capital Supply upkeep removed; War Economy +10 Supply and Martial Culture +10 Manpower each Logistics Cycle; Salvagers 2 Supply on victory, 1 on defeat/draw, retaining +1 capture and no uncontested-bombardment/unguarded-strike reward; Swift loses its Expand bonus but retains creation at 5 for 1 Supply/1 Manpower and half ordinary-fleet upkeep (explicitly confirmed); Void expansion remains +4 for 0 Supply/1 Manpower. Siege halves base Ground Assault Supply cost, rounded up (1/1/2/2), other Siege benefits retained. Dread charges the existing 1+2 per participating asset in BOTH Supply and Manpower, once per combined engagement, additive to combat commitment and never refunded as committed personnel. Fortification restores exactly 4 defence on every world/station, capped at maximum (Capital Defend amount, explicitly confirmed), retaining free Defend, Defended and +2 Supply. Industrial retains discounted costs and new-project Integrity 2, but subsequent Build/Upgrade adds only 1. Other trait benefits remain.

Bot attack affordability, Dread resource budgeting, normal Swift restoration forecasts, Fortification recovery estimates and Industrial completion/survival forecasts updated to match. The separate inspection recommendations about pursuit/delivery loops, Scout complementary investment and explicitly chosen project schedules remain unimplemented. The prior suggested Dread fixed charge 2 and Swift creation Supply cost 2 were NOT applied: the creator specified a different package.

Validation: 568 regression tests passed (including 13 new focused tests with tier/action/outcome subcases), plus four two-Cycle synthetic smoke traces spanning all twelve traits, 136 commands independently replayed exactly. These are mechanics checks, not balance campaigns. Verified all 201 source candidate files and 29 accepted-baseline inputs unchanged. First regression output retained; intentional updates to obsolete expectations are listed in intentional-test-updates.json. No old game outcomes were overwritten or reinterpreted. No timers, automated follow-ups, publication, or campaign batch launched. Suspended Dessica remains unchanged. New balance results are required before claiming the creator's 25-percentage-point trait spread target is met.

## 3 October 2026 — recovered-package FULL MANUAL INSPECTION COMPLETE

Read recovered-package-study-20261003/Full_Balance_Inspection_2026-10-03.txt and MANUAL_INSPECTION_COMPLETE.json. All72traces/55,423saved orders covered,264integrity checks; additional2562exact-prefix orders replayed,21saved decisions/568construction alternatives,7200deterministic player setups. No new campaigns, code/rule edits, timers or publication.

Verdict: observed44.4pp trait spread still exceeds25pp. Rates/9: Salvagers5,Swift5,Efficient4,Industrial3,Martial3,Void3,Fortification3,Siege2,Endurance2,Mobile2,Dread1,War1. Mobile/War each survive2censored games, not wins.34resolved mean59.44Cycles;16within50–100,15below,3above;2censored200. Non-Mobile27games average52.26;Mobile9average112.22. Case17 remains a four-fleet shuttle/no combat loop; case3lands9successful assaults in final30Cycles but target repairs. Neither accepts late truces. Movement/delivery, funded Scout+strength combinations and explicitly chosen construction schedules need correction, not extra War income or forced Mobile suicide.

Constructions ever-active43.3→48.2%; never-active spending share30.9→25.0%.System construction delivery/tenunused profiles remain unresolved.568saved alternatives:unused defence/escort had no positive sampled scores;Consolidation no legal sampled options. No blanket discount recommended. Supply shortage4.36→4.53%,Manpower3.42→3.12%;zero self-action deficit triggers;largest increases attributable to enemy assaults/events with little/no recent construction. All three routes used;no human win-rate claim.

Recommended ONLY: Dreadfixed2+2perasset;Swiftcreation2S/1MPready5;Salvagers2Swinning/1Slosing-drawn,+1capture(moderate exploit-focused change, map-sensitive evidence);retainother9traits. Couple with reachability/Scout complementary upgrade/real construction schedule corrections, qualify saved situations before a newcomplete roster batch. Unimplemented;no automatic run. Existing POSTPROCESSING_COMPLETE said manual pending at batch completion; this newer completion record supersedes that status without rewriting evidence. Accepted baseline and Dessica unchanged.

## 3 October 2026 — recovered-package screen COMPLETE; full manual verdict pending

Checked at22:38Sydney. All36 new candidate games completed and independently replay-validated,29,849 new orders;36 exact saved controls retained. No failures or remaining Python runners. Automatic summary, all72-trace inspection and paired comparison completed at22:19:32, about58minutes after launch. POSTPROCESSING_COMPLETE.json retains manual_verdict_pending=true. Do not restart or launch a follow-on automatically.

Initial read only: candidate34 resolved games,2 censored at200Cycles;16 finish within50–100,15 below50 and3 above100. Resolved mean59.44Cycles; all-game median53.5. Observed trait spread44.44pp still exceeds25pp target; nine appearances per trait gives11.11pp per win. Salvagers/Swift5wins each, Dread/War Economy1each; War Economy and Mobile also each survive2 unresolved games, which are not victories. Need full paired causal inspection before new changes. Supply shortage exposure4.53% versus4.36%; Manpower3.12% versus3.42%; zero voluntary-order deficit triggers in either arm. These are aggregate findings, not a balance sign-off or human Soulstorm prediction. Root baseline, prior evidence and suspended Dessica unchanged.

## 3 October 2026 — complete recovered-package comparison RUNNING

User approved the new complete36-case comparison after the planning/ceasefire diagnostics. Directory: recovered-package-study-20261003. Started 2026-10-03T21:21:29+10:00; wrapper PID 7696, study PID 20572. One worker;36 NEW candidate campaigns plus36 retained matching controls from release-package-study-20261003/candidate. This is one complete screen, not a stage. Estimated90–120minutes from launch, approximately22:50–23:20Sydney; estimate only, not a cutoff or permission to drop difficult cases. No timer, reminder, publication or automatic next batch.

Candidate copied exactly from planning-recovery-20261003/pact-check/candidate, including the approved full audit package and subsequent qualified bot/replay corrections.555 regression tests rerun successfully in the new location (44.857s);12 new harness checks pass.145 baseline/old-study hashes verified. Both engines and all analysis/runner/schedule inputs frozen in manifest. Original failed72-game arm, saved continuations, accepted baseline and suspended DessicaCycle21 remain separate and unchanged.

36-case predeclared balanced prefix, nine appearances per trait and three per seat;24 matched/12 generated maps, six/three appearances per trait in those families. Controls are retained evidence, not36 new completed games. Check manifest.new_games_completed and results/candidate file count. A new row is written only after exact replay verification. Worker processes run sequentially and release memory between games. A failed game now produces nonzero exit and halts before starting the next; wrapper refuses analysis until all72 paired rows and successful replay counts exist. Do not duplicate or mutate frozen inputs while running.

Check progress.txt, manifest.json, wrapper-errors.txt and batch-error.txt if present. On completion run_batch.py automatically runs summarise.py, inspect_full.py and paired_outcomes.py; POSTPROCESSING_COMPLETE.json confirms evidence processing but explicitly leaves the manual verdict pending. Inspect all12traits/25pp target,50–100Cycle pacing, Mobile pursuit tails and ceasefires, shortages/contexts, construction delivery/loss/spend and attack choices. Censored survivors are never wins; summary includes unresolved-survivor bounds and paired unresolved categories. One win here changes the observed rate11.11pp; no precise parity certification or inference to human Soulstorm win rates. Comparison is combined package versus previous release candidate, not an isolated estimate for each correction. Plan in Study_Plan.txt; exact control provenance in reused-reference-provenance.json.

## 3 October 2026 — planning and ceasefire checks COMPLETE

Read planning-recovery-20261003/Planning_Recovery_Results_2026-10-03.txt and final-inspection.json.555 regressions pass;6 saved hypothetical choices legally resolved,332 alternative forecasts checked. Planning-only correction and subsequent ceasefire correction retained as SEPARATE frozen candidates. Three new30-Cycle continuations each, exact prior starting states/dice seeds; reused controls labelled. New replay-verified orders:805 plus630. Final correction resolves1/3 within30 additionalCycles. Not fresh campaign wins or trait parity evidence.

Both requested defects fixed: Mobile Capital construction objectives and cap-aware gross-income-before-upkeep forecasts/marginal economic value. During inspection found repeated ceasefires: planning-only case11 accepted10 and case14 accepted14 in30Cycles. Isolated pact-check candidate fixes strength comparison across surviving forces while preserving shortage/deficit/local-threat recovery. Previous case14 Scout audits used every viable opportunity; no arbitrary attack mandate or movement/rules nerf. Full baseline/previous study hashes145 and current input pins checked. Original failed72-game arm preserved and incomplete. No full batch running or automatically queued; no timers/publication/Dessica changes.

Manual verdict: latest pacts0 in all3; case14 resolves5Cycles, case11 ends Mobile2strength versus10, but case3 now unresolved at30/Mobile3strength versus previous victory18. Do not conceal that counterexample or treat low strength as victory. Recommend retain the combined candidate for a newly labelled COMPLETE balanced36-game screen with exact saved references, runtime sized under the two-hour allowance. Assess long tails honestly, alongside all traits and economic/construction metrics; no more tuning these three examples to force wins. This is a recommendation, not a launched batch or balance sign-off.

## 3 October 2026 — ceasefire follow-through checks RUNNING

Both approved planning corrections are implemented and their first three paired continuations COMPLETE in planning-recovery-20261003: case3 resolves18 extraCycles versus30, cases11/14 remain unresolved.555 tests now pass in nested pact-check/candidate after adding6 ceasefire safeguards; earlier549 planning suite also passed. Inspection confirmed10 accepted truces in case11 and14 in case14 prevented operations despite healthy larger pursuing forces. Bot compared the empty destination system rather than surviving faction forces. This is a policy issue, not an invented campaign truce restriction.

A separate pact-check candidate changes only that strength comparison; retains shortage/deficit/immediate-threat safeguards. Frozen planning-only results preserved. Three new30-Cycle continuations from the SAME Cycle200 states and seeds versus reused planning-only controls. Parent11680 started about20:57Sydney. Check pact-check/continuations-progress.txt and qualification.json; no full campaigns or automatic next batch. Case3 currently remains unresolved at230 with enemy Mobile Capital at3 strength: don't label it fixed or a demonstrated regression from censored outcome alone. Wait for11/14, inspect combat/construction/truce evidence; run finish_inspection.py only after all three finish. That script validates frozen input/reference hashes and writes the final report/notes. No timers, external publication, baseline or Dessica changes.

## 3 October 2026 — planning corrections implemented; short paired checks RUNNING

User approved proceeding with both confirmed defects. Isolated planning-recovery-20261003/candidate adds Mobile Capital construction objectives and probes their real ground resolver/costs/defences; forecasts capped gross income BEFORE upkeep; prices economic construction using marginal retained/usable income against the same funded expenditure schedule. Forecast resource weighting also respects the cap. No mechanics, traits, prices, original evidence or Dessica changes.

549 regression tests passed (12 new). Two prior demand/timing fixtures had saturated unspent resources; adjusted to genuine spending demand without weakening the assertions. Initial failures retained. Six frozen end-position hypothetical construction choices legally submitted after explicitly releasing the already-spent construction phase in isolated clones;332 alternative forecasts checked. This is not an extra action in the historical campaigns. Saved-check first attempt correctly failed because the historical phase was already spent; preserved log. Candidate checks never mutate source snapshots.

Three new30-Cycle continuations from EXACT original stalled Cycle200 states, same diagnostic seeds, versus three reused validated pursuit-recovery corrected-bot controls. Parent13740 started around20:43Sydney; single worker, expected10–15minutes. No full campaign batch or automatic next batch. Engine and reference hashes in qualification.json. Check continuations-progress.txt and six JSON/trace outputs (three controls already present). Do not duplicate or change candidate files while running. Every new continuation replay-validates all orders. Case3 already resolved for pursuer in18 extra Cycles versus30 in previous correction.

Additional prior-case14 replay audit verified both final states: original bot had6 viable Scout decision opportunities and used all6; earlier correction had2 and used both. Zero viable Scout alternatives ignored in those traces. Do not force extra attacks to match counts; changed situations/action availability explain fewer opportunities, not a demonstrated skipped legal attack. Evidence case14-interception-*.json. On completion inspect all3 pairs, purchases/completions, remaining strength and resource use; preserve unresolved outcomes. No win-rate inference from these saved continuations. Full balance batch still stopped.

## 3 October 2026 — recovery inspection COMPLETE; two planning defects remain

Read pursuit-recovery-20261003/Recovery_Findings_2026-10-03.txt. All six paired saved-position continuations completed and replay-validated,2290 orders. No simulations remain running; no replacement full batch launched. Case3 correction resolves for the pursuer while control stays unresolved. Cases11/14 remain unresolved in both versions. Pursuit moves187→56,215→81,284→108; Mobile assaults0→14,0→4,6→2 respectively. Do not call all pursuit stalls fixed or treat these as fresh campaign trait wins.

537 regressions and four failure-gate checks pass.34 hashes and230 replay orders match the direct canonical digest; measured temporary digest allocation reduces84% (not whole-process memory), with modest instrumented runtime cost. Original failed16 separately recovered and independently replay-validated2436 orders at157Cycles. Original MemoryError cause remains unconfirmed. Failed72-game arm stays frozen/incomplete; retained17 results unchanged.

Read-only end-position inspection confirms two remaining bot defects: military construction target selection omits Mobile Capitals ('no ground objective' despite legal fleet upgrade choices), and construction forecasts accumulate impossible stocks above the existing100 cap (e.g894Supply/303Manpower) and feed these to combat estimates. Economic valuation also credits nominal income without marginal overflow accounting. No fixes to these two defects implemented yet. Recommend correcting both together in a separate candidate, checking Mobile/ordinary targets and cap-aware economic/operating alternatives, then brief paired continuations including case14. Avoid forcing victories or polishing bots until every legitimate long game vanishes. No long batch until that qualification; next whole-roster experiment needs a new complete balanced design within two hours.145 protected hashes and mechanical pins unchanged. No trait/rule/price changes, baseline promotion, Dessica advancement, timers or publication.

## 3 October 2026 — PC restart recovery; short checks running

Checkpoint 2026-10-03T20:09:17+10:00. Read pursuit-recovery-20261003/Recovery_Checkpoint_2026-10-03.txt. Original audit-package study remains failed/frozen; no replacement campaign batch is running. Saved evidence survived the PC restart. Recovery candidate only: lower-allocation byte-identical digest, surplus pursuit containment, existing Scout interception priority/valuation. No game-rule changes. Scout attacks on Mobile Capitals were ALREADY legal; earlier suggestion otherwise was corrected.

537 regressions passed; four runner-gate checks passed;34 snapshot hashes and230 replayed orders matched; measured digest temporary allocation reduced84%, not whole-process memory. Original failed16 reproduced to157Cycles before restart; independent replay is still pending unless original-case16-validation.json now exists. Invalid zero memory counters are not evidence of peak usage.

5/6 paired30-Cycle continuations recorded and replay-validated at checkpoint. Case3 correction resolves versus stuck control; case11 remains unresolved but215 pursuit moves become81 and0 Mobile assaults become4. Wait for case14 and inspect all six before verdict. Processes at checkpoint: continuations.py parent3120; original verification16248 (PIDs are historical, verify before acting). Progress: continuations-progress.txt; original-case16-validation-log.txt. Do not duplicate. Run inspect_recovery.py after completion.145 protected hashes unchanged; no baseline/Dessica changes, timers or publication. Do not resume the old55 remaining under changed code or claim a completed balance test.

Original sample16 independently replay-validated: 2436 orders at157 Cycles, retained separately from the corrected candidate.

## 3 October 2026 — audit-package screen STOPPED after recording failure; ETA withdrawn

Read audit-package-study-20261003/Interruption_Inspection_2026-10-03.txt. Status is failed, no runner remains active and no restart was launched.17/72 new games replay-validated (18680 orders);14 resolved, three censored at200Cycles (cases3,11,14).55 remain unrecorded, including failed16. Sample17 finished while the failure queue drained. All72 references and frozen input hashes remain intact.

Sample16 MemoryError occurred in snapshot json.dumps during order digest. Allocation cause remains unconfirmed. Wrapper subsequently attempted summarisation because study.py returned0 after failed status; summarisation failed safely with missing results.json. Preserve manifest/error evidence and originals. Three censored cases show Mobile retreat plus repeated all-force pursuit; the new survival qualification missed this opponent interaction. Case17 resolved at145. Original8:05pm/two-hour ETA is invalid. No reliable replacement ETA until recovery qualification; do not automatically launch55 remaining games or silently shrink/relabel the study.

Recovery recommendation: saved-position containment/pursuit qualification (no forced Mobile suicide or new movement rules); memory profiling and byte-identical incremental digest qualification; corrected external failure gate; then a freshly estimated COMPLETE balanced screen respecting user's two-hour allowance. No balanced win rates from partial/censored survivors. No baseline/Dessica changes, no timers/publication.

## 3 October 2026 — approved coordinated package; two-hour comparison launched

Implemented the complete historical-audit recommendation in isolated audit-package-study-20261003: Dread1+2/asset; Swift ready5 creation1Supply/1Manpower; Siege victory refund bonus+2; Mobile survival/shipyard retreat correction; system-project ground-control-loss forecast and consistent continuation/new-start comparison. Efficient6, Fortification and other current construction/trait rules retained. Candidate guide corrects Salvagers prose to match the existing all-ground-participation effect. Nothing promoted to the accepted campaign baseline.

531 tests and32 saved-position checks passed. Five historical losses were independently replayed first (4437 orders). Ten formerly idle threatened Mobile positions now choose legal retreats; the20 sampled construction decisions remain unchanged. These checks do not claim recovered wins.

One complete72-new-game comparison against72 exact saved references started 18:02 local; expected90–120minutes including replay validation and automated inspection, check back around20:02.18 appearances per trait, six per seat, balanced map families. No stages, reminders or automatic next batch. User's25pp trait-spread target, pacing, resource shortages, all attack choices and construction delivery remain the acceptance checks. Results are pending; this note is not a balance claim. Dessica remains suspended and unchanged.

## 3 October 2026 — full historical audit; proposed coordinated balance package

See Cross_Testing_Audit_and_Balance_Package_2026-10-03.txt. The latest roster still fails the creator's25-percentage-point spread (45.8%→12.5%). Historical result versions remain separate; copied controls and unresolved survivors are not extra wins. The audit indexes104 aggregate result files and9,961 individual cases and adds fresh all96-current-game calculations; this is not a claim of replaying every historical game.

Proposal only, not implemented: Dread surcharge1+2/asset; Swift ready5 creation1S/1MP; Siege victory return floor(60% commitment)+2+best Transport bonus, capped at commitment; correct Mobile escape/survival decisions and system-project control-loss/continuation assessment. Retain Efficient6, Fortification enhanced free Defend+2Supply, and current middle-trait, construction-price, economic and attack-route settings. Do not restore automatic holding-defence overrides or force project completion. Retain Militia Major5 at2Supply/action: an untested Minor3 conversion loses meaningful durability. Current candidate is not promoted to accepted rules by this note.

Historical review changes the previous Efficient rollback recommendation: cutting6→5 removes764 resources on latest recorded states and repeats a previously weak setting. Proposed Dread cut reduces nominal paid tax15.4% while preserving per-asset strength; Swift's one-personnel cost preserves its large tempo/upkeep advantages; Siege extra refund benefits111 of355 latest victories, with no added defeat capture power. Counterfactual wins remain unknown. Industrial's inexpensive accelerated economic upgrades are a deliberate player exploit-check priority, not proof it needs another buff.

All33 constructions are covered in the report. System-control changes, including107 Storm Transit and27 System Repair events following ground orders, expose ownership risk omitted from part of the forecast; these are not all direct damage or incomplete projects. Recent lower prices alone do not establish value. Keep the accepted50–100Cycle design direction and attack alternatives;31/96 current campaigns still end under50 and must not be described as rare exceptions. Human Soulstorm difficulty, Sector and mod project remain deferred.

No new campaigns, timer, publication, rule edits or Dessica changes. Proposed next complete36-game screen has nine appearances/trait and equal seat exposure; original first36 took37.23minutes including replay, so45–60minutes is a planning estimate, not a guarantee. Earlier24-game lower-runtime option remains available before launch. No stages; larger fresh confirmation comes after the screening target, as requested.

## 30 September 2026 — user ACCEPTED station-only baseline; defence experiments set aside

User: "I agree with your recommendation." Accepted working candidate: holding-defence-study-20260930/station. Pinned in Accepted_Balance_Baseline_2026-09-30.json; hashes verified. Both holding-defence experiments remain preserved, not promoted. No published rule changes or full-balance sign-off implied.

Next work is targeted construction value/delivery and whole-roster evidence review, detailed in Next_Targeted_Balance_Work_2026-09-30.md. Prioritise Militia/shields and system stations, retain fleet-support/unused catalogue coverage, use larger primary trait evidence rather than tuning against failed policy variants. No new prices/trait numbers or long batch authorised by this acceptance. No timers or publication. Current Militia notes and implementation agree: only Defend Manpower cost is waived, normal Supply remains; a briefly suspected discrepancy was a reading error and has been corrected.

## 30 September 2026 — defensive reserve comparison COMPLETE; station-only remains preferred

Report: defence-reserve-study-20260930/Defence_Reserve_Results_2026-09-30.md. All 48 new games plus 48 reused controls,70,299 validated orders/35,703 new; no failures or censors. All 96 traces inspected:1,498 projects,498 deficit entries. No new independent decision replay this inspection. Frozen/paired/root hashes checked; Dessica preserved.

Reserve guard partially improves unguarded defence: deficits 283 to 259, but station-only 239 remains better. Supply exposure 5.85% versus 5.23%; active 333 versus 343; never-active spend 2411 versus 2057. Mean 57.21/median 54.5, target 28/48 versus 32/48. Swift 3/12 versus 2, Efficient 9,Dread 0; not trait-parity evidence. Station completion remains weak. All main attack routes used.

Recommendation: keep station-only (holding-defence-study-20260930/station) preferred; preserve both defence experiments without promoting. Stop refining this optional override as a prerequisite; return to outstanding construction/trait questions using saved/equal-resource evidence and larger prior studies. No automatic further batch, timer, publication or numerical rule changes. Full readiness remains unproven. User has not yet approved the next recommendation.

## 30 September 2026 — defensive reserve comparison RUNNING

User requested "Please carry on" after local qualification. Started defence-reserve-study-20260930/study.py --start at approximately09:56Sydney,30September2026; mainPID5128. Manifest running, two workers, no startup errors. Do not duplicate or modify frozen inputs. Read Study_Plan.md in that directory.

48 NEW reserve-aware holding-defence games versus48 exact verified station-only controls;96records/48pairs. All12traits have12appearances per version,24matched/24generated scenarios. Same reused secondary schedule, NOT fresh holdout evidence. Every new game replay-validated; pair initial hashes match; extra holding_protection.py pinned in frozen checks and each worker. Previous unguarded version available for scenario-matched descriptive comparison. Failures retained and scheduling stops;200Cycle horizon.

ETA45–75minutes execution, approximately10:41–11:11Sydney, plus20–30minutes inspection. No timer/reminders or publication. Initial48/96 reflects ONLY reused controls,zero new completions. Check progress/errors without interrupting healthy processes. On completion inspect shortages, rationing, territorial retention, construction delivery, all traits, route choice and duration; audit reserve guard decisions. Do not assume local qualification establishes campaign balance or human Soulstorm outcomes. No automatic further batch. Root protected hashes and suspended Dessica unchanged.

## 30 September 2026 — defensive reserve correction locally qualified

Report: defence-reserve-review-20260930/Defence_Reserve_Qualification_2026-09-30.md. Isolated candidate adds defensive-cost and next-Logistics buffer checks plus existing resource-scarcity weights to experimental holding protection. Campaign-tested preferred version remains station-only; this candidate is not yet campaign-validated. No rule/trait/price changes, timer, publication or new batch.

515 full regressions passed. Six saved states, 41 alternatives plus six selected and six wrapper public submissions checked. Useful case25 Cycle26 still Defends; four low-value choices remain unchanged. Latest case34 Cycle22 now retains Muster rather than Defend leaving1MP: conservative buffer fails and weighted opportunity cost is negative. Original strategy budgets used, snapshots saved. Prior wrong-directory fixture failures retained; correct-directory suite passed without weakened tests.

Next: bounded comparison against verified station-only controls if authorised, examining shortages/retention/constructions/all traits/duration. Reserve estimate covers one visible assault per hostile faction/system and next negative Logistics net; not repeated attacks, future arrivals or random events. Positive income not borrowed early. Longer-term holding income is not newly modelled. Old study frozen and six protected root hashes verified; Dessica preserved.

## 30 September 2026 — three-version balance inspection COMPLETE

Report: holding-defence-study-20260930/Holding_Defence_Balance_Inspection_2026-09-30.md. All 144 records (96 NEW/48 reused controls),105151 orders; no failures/censors. All traces inspected; additional five adverse-game replays 5930 orders/1204 Faction decisions/34 overrides. Recomputed choices matched 1204/1204. Frozen/root hashes intact; Dessica preserved. No new batch, timer, rule edits or publication.

Verdict: retain STATION-ONLY correction; do NOT promote combined holding-defence policy yet. Station never-active spend 2147 to 2057, active 342 to 343, no winner changes. Combined versus station: deficits 239 to 283; Supply exposure 5.23 to 6.59%; active 343/733 to 334/783; never-active spend 2057 to 2359. Mean 56.10 to 58.33, target 32/48 to 30/48; no terminal inactivity. Swift 2/12 unchanged; Efficient/Salvagers 8/12,Dread 0/12. Small reused schedule is NOT trait-parity proof. All routes used. Stations and unused profiles remain unresolved.

Recommendation ONLY: retain useful defensive option but guard overrides with existing reserves/known Logistics and credible involuntary defensive costs; avoid marginal short-lived repairs replacing recovery. Case 34 Void Defend left 1 MP, enemy attack triggered deficit nextCycle; case 4 Swift repaired holdings lost 1–2 Cycles later. Qualify locally against useful/futile/capital/deficit cases before any approved batch. Station-only code at holding-defence-study-20260930/station; combined remains frozen experimental evidence. No automatic further batch.

## 30 September 2026 — bounded holding-defence comparison RUNNING

User requested "Please begin". Launched holding-defence-study-20260930/study.py --start at 01:19:43 Sydney, 30 September 2026; main PID20156. Manifest running, two workers, no startup errors. Do not duplicate, modify frozen inputs or rerun preparation. Check current manifest/process rather than assuming the PID remains live.

48 scenarios, three versions: control (prior construction-forecast candidate), station correction only, combined station plus selective holding defence. 48 exact verified historical controls reused, 96 NEW games; 144 records total. Every trait has12 appearances per version;24 matched/24 generated scenarios. Schedule reuses historical secondary cases144–191, NOT a fresh holdout. Initial states must match across three versions. Each new game replay-validated; frozen hash check includes holding_protection.py in combined candidate. Failures recorded and scheduling stopped; no dropping cases. 200-Cycle horizon.

ETA1–2hours for execution (roughly02:20–03:20 Sydney), then20–30minutes inspection. No timer or reminders. On status requests keep healthy runner alive. After completion compare station/control, combined/station and combined/control; examine all traits, holding retention, resources/capital cascades, construction activation, three attack routes, campaign duration and censoring. No human Soulstorm inference or automatic additional batch. Protected root hashes match; suspended Dessica preserved. Plan: holding-defence-study-20260930/Study_Plan.md. At startup48/144 means reused controls, ZERO new games completed; do not describe it as one-third through new computation.

## 30 September 2026 — selective holding defence implemented and locally qualified

Report: holding-defence-review-20260930/Holding_Defence_Qualification_2026-09-30.md. Candidate inherits the staged station forecasts and adds a trait-independent operational Faction Action comparison. Preserve compulsory capital/deficit and fleet-recovery priorities. Compare legal Defend and safe garrison transfer against the original action after costs; require material capture-risk improvement and positive benefit after forgone resources/fleet strength. No Swift or gameplay numerical changes.

503 full regressions passed; focused suite 14 passed after six additions (509 distinct tests overall). Five saved positions: 36 original-or-Defend and five selected public submissions checked. Four choices unchanged; case 25 Cycle 26 now Defends holding 3 from 1/4 to 3/4 against two visible damage, instead of Muster. This is a single-assault model benefit, not a changed campaign outcome. Protected root hashes match; Dessica preserved.

No long batch, timer or publication started. Candidate ready for an approved bounded paired comparison, inspecting retention, shortages/capital cascades, construction completion, all traits and duration. Station and defence corrections must remain distinguishable in attribution. Previous candidates and studies frozen. Legacy non-operational controllers remain unchanged; all traits using operational chooser receive correction. Read report for provisional scoring thresholds and limits.

## 29 September 2026 — Swift territorial-retention inspection complete

Report: station-swift-review-20260929/Swift_Retention_Inspection_2026-09-29.md. Replayed 18 saved games (all nine lost-win pairs), 14,488 orders; final digests matched. Five saved decisions and 36 public alternatives checked. No new campaigns, bot/rule changes, timer or publication. Candidate losses by Cycle 24: 63 versus control 50. This selected subset cannot establish general win rates.

Verdict: no immediate Swift buff. Recommend a general selective holding-defence comparison, not automatic Defend. Case 25 Cycle 26: affordable Defend raises a 1/4 holding above visible two-damage assault (model capture risk 80.5% to zero). Case 8 Cycle 11: repair leaves model capture certain. The current chooser chiefly prioritises capitals and project hosts; ordinary holding defence depends on strategy consolidation and surplus resources. Compare legal Defend, garrison transfer and the existing choice after costs; preserve compulsory capital and deficit handling. Retain resupply or recruitment when repair achieves little. This recommendation is NOT implemented. Qualify saved useful, futile and resource-sensitive cases before an approved batch. The earlier station forecast correction remains staged. Protected root hashes verified.

## 29 September 2026 — station forecast correction and Swift saved review complete

Report: station-swift-review-20260929/Station_Forecast_and_Swift_Review_2026-09-29.md. Isolated candidate only; 495 regressions passed, 1,388 frozen replay orders reconstructed five station positions, ten legal public submissions checked. Repair forecasts now account for affordable pooled shipyard repairs before activation; defence forecasts discount one sufficiently favourable legal naval-clearance opportunity. Case44 Cycle3 switches Repair Station to Cannons; other four sampled choices unchanged. Station completion/value is not globally validated.

Swift: all48 paired appearances/96 traces inspected; wins14 to8 (nine lost,three gained), early expansion almost identical, Cycle24 holdings4.458 to4.167 despite cumulative captures9.083 to9.146. Seven of nine lost wins first diverge on opponents' orders. No immediate trait buff recommended; next narrow inspection is later holding losses/retention choices, not another broad bot rewrite. No new campaign batch, rule/price edits, timer or publication. Six protected root hashes verified; suspended Dessica preserved. Only staged construction_coverage.py changed among existing production files; nine tests added. Evidence and limitations are in the report.

## 27 September 2026 — approved whole-roster package implemented and comparison running

User approved the combined proposal and requested implementation/testing. Work directory whole-roster-candidate-20260927. Read Qualification_Report_2026-09-27.md and Comparison_Plan_2026-09-27.md. NO duplicate runner, no timers/reminders, no publication. Preserve all prior studies, root rules/draft/code and suspended Dessica. The candidate is isolated; final source consolidation follows results, not before.

Implemented: Swift rounded-up half ordinary fleet count upkeep of each resource; Mobile self-Expand for 1 Supply/1 Manpower/up to 2 defence using Fleet Action; Siege +1 committed Manpower returned on actual ground victory; Transport +2/+4 victorious return, best only and total capped at commitment; Salvage Wing/Storm Transit 3 Supply stage cost with five stages; completed Militia/Void Shield base persists at positive Integrity, upgraded Shield bonus at full upgraded Integrity. Existing isolated-defender non-victory recovery receives no new bonus. Dependent construction valuations use the updated return formula.

Bot correction: System Repair demand at completion credits known automatic recovery, funded builder restoration, current target departures and earlier funded local stations; no imaginary future damage/arrivals. Repair Tender uses the same known-damage projection while retaining its existing local naval-exposure estimate. Grand Yard forecast remains unchanged. Mobile refit considered before discretionary movement but after immediate feasible combat; saved combat-ready states still chose attacks. Pilot94 actually used mobile self-refit once. Do not claim optimal trait adoption.

Qualification: 422 regressions (405 old +17 new), 6 edge checks passed. Initial logs retain transient indentation error and five outdated rule expectations, then full suite passed. Fixed-rule fixture intentionally refreshed only in candidate. Saved comparison:46 ground positions,8 Mobile positions,15 construction decisions, both arms nonmutating. Six mobile positions newly legal. Replayed3 prior games/3278orders to inspect16 repair starts (overlap previous evidence, not fresh games):9 previously positive starts become negative,6 unchanged,1 weaker positive. Cases and rationale saved. Five full pilots validated: candidate24=63Cycles/849orders;45=37/426;94=66/913;144=40/528;freshcontrol144=38/519. Fresh pair initial hashes identical. Pilots count once inside batch.

Comparison:192pairs/384results =144 exact reused control games +240 newly simulated games. Primary144pairs same historical schedule,36appearances/trait/arm,12perseat,18permapfamily. Fresh confirmation48pairs,12appearances/trait/arm,4perseat,6permapfamily, new seeds. Report cohorts separately; do not call384freshgames or pool repeated historical controls as independent. Two workers,200Cycle safety horizon. Frozen inputs and harness hashes enforced, every new game replay-validated, explicit failures retained. Control provenance in control-reuse-manifest.json. Check manifest/progress/stderr read-only; leave normal runs alone. Results written only after all384 validated and initial pairs match.

User ETA: check back about2.5hours, allow3hours from launch. No notification automation. On completion inspect all12traits, construction delivery/value and synergy (Industrial4Supply base Wing/Transit; Endurance/Salvager cheaper Wings; Siege/Transport full refunds; Fortification persistence), both deficits, voluntary-spending invariants, duration/tails, ground/naval/bombardment and bot adoption. No automatic further batch. No human Soulstorm win-rate inference; global difficulty question deferred. Prior review report remains historical rationale, not current completion status.

Verified launch: 2026-09-27T22:54:45.145110+10:00, main PID 10352. Verify current process rather than assuming this PID is still live. Snapshot: 151/384 compared results, running, 0 failures.

## 27 September 2026 — whole-roster and construction proposal; not implemented

User approved reviewing all twelve traits together with construction value. Full proposal: whole-roster-review-20260927/Whole_Roster_Package_Proposal_2026-09-27.md. PROPOSED ONLY: no new numerical rules implemented, no campaign batch, timer or publication. All review processes finished. Protected source/draft/root simulation files and suspended Dessica remain unchanged; review-preservation.json verifies six protected files and current study manifest inputs.

Evidence: all 144 corrected traces/432 Major runs analysed. Independently replayed 12 winner-selected diagnostic games (one winner per trait, also losing appearances), 8,718 orders; 276 local ground positions and 19 damaged Mobile turn starts. Three additional saved games replayed, 3,278 orders, 67 construction starts including 22 military and 16 System Repair starts. These overlap the previous inspection and are not fresh campaigns or independent confirmation. Arithmetic checks cover 20 upkeep sizes, 30 return cases, 10 prices, 6 Integrity states and 13 reward schedules. Exact saved states and JSON evidence accompany the report.

Propose Swift upkeep ceil(living ordinary fleets/2) of EACH resource, keeping full creation/Expand; Mobile Expand itself for 1 Supply/1 Manpower restoring up to 2 defence, spending its Fleet Action with no Defended; Siege +1 committed Manpower returned on actual victorious Ground Assault only, after normal/best Transport, capped at commitment. Keep the other nine traits with explicit reasons; Void and War remain watch cases for Manpower pressure. No leader nerfs or extra defeat damage.

Propose Transport extra victorious return +2/+4 instead of +1/+2, best only and total capped at commitment; Salvage Wing and Storm Transit stage price 3 Supply instead of 5 while retaining five stages/Integrity; completed Militia Barracks and Void Shield retain base effects at positive Integrity (upgraded Shield bonus still requires full upgraded Integrity). All other construction numerical effects remain. These changes also benefit leaders: Industrial new base Wing/Transit costs 4 Supply over four actions; Endurance/Salvagers cheaper Wing and Siege/Transport full refunds must be explicit comparison cases.

Narrow bot correction proposed: System Repair demand should be valued at completion, accounting for known recovery, funded repair and expected fleet location, without counting the same existing damage for multiple unfinished stations. Observed 16 starts forecast 5–22 Cycle completion delays. None of 22 military starts failed current 0.5 survival threshold, so do not claim a broad missing survival screen is the demonstrated cause. No new general bot rewrite or purchase quotas.

Next: await user response to concrete proposal. If approved, implement isolated combined candidate, qualify saved situations/action use/deficit locks/returns/positive Integrity/Industrial prices, then one bounded all-twelve comparison including construction interactions and fresh confirmation coverage. No claim of achieved balance or predicted human Soulstorm win rates. Keep core campaign duration/resource/attack route direction.

## 27 September 2026 — release inspection completed

Full report: release-corrections-20260927/Release_Inspection_2026-09-27.md. All144 corrected games completed against144 exact reused controls. All288 traces inspected, with24 saved games independently replayed (22,958 unique historical orders). No new rule changes or campaign batch started during inspection.

Keep the core direction: median54Cycles, average56.87, no censored endings; all three attack routes used. Supply/Manpower deficit exposure falls to4.71%/3.86%; no voluntary self-caused deficit entries. Garrison reversals fall808→18 with no prolonged five-action run. Defensive preparation improves: OrbitalCannons339active from378starts, versus4active previously.

Full roster still fails reasonable parity: Endurance/Salvagers22wins each, Swift3, Siege/Mobile6 each, per36appearances. Other counts and uncertainty are in the report. Swift's full-strength creation actually works; its resource pressure remains highest. Prefer bounded sustainment/capital-recovery improvements for the weakest traits over indiscriminate new damage or automatic leader nerfs. AI success does not establish human Soulstorm difficulty.

Construction issues are specific: service projects are often legal to finish but lose projected local value; damaged fleet hosts block ongoing military/Salvage work. Nine profiles remain unpurchased, which requires niche/equal-budget assessment rather than a popularity quota. GrandYard9/10activations and actual production are encouraging. VoidStation has2successful conversions: generic zero-active counts must not be reported as zero completions. See report for full dispositions and attribution limits.

Verdict: keep bot corrections/core rules; targeted trait and construction tuning remains before signing off the full roster. No general bot-perfecting loop or automatic further batch. Consolidate the approved additive rules/briefings before campaign restart. Root rules, frozen studies and suspended Dessica remain unchanged.

## 27 September 2026 — release corrections implemented and comparison started

User approved targeted corrections and bounded verification before release. Changes are isolated in release-corrections-20260927; no numerical campaign-rule changes. Garrison choices now consider donor loss and rebuild an absent fleet; defensive construction value is conditional on surviving unfinished stages, with visible future threats considered; Consolidation also credits permanent defence.

405regressions and4exact saved-position checks passed. Qualified pilots resolved old200Cyclecase104in36Cycles and case8in49versus88; these are diagnostics, not global results. The new comparison runs144corrected games against144exact reused controls on the balanced schedule. Two workers; started20:03:55Sydney. No timer or automatic further batch. Read the qualification report for exposed bot probability assumptions and preservation details. The full prior inspection remains valid historical evidence; final trait/whole-package verdict awaits this correction comparison.

## 27 September 2026 — completed construction/trait package inspection

Full evidence/report: construction-trait-qualification-20260927/Full_Package_Inspection_2026-09-27.md. All288game records and24deep paired replays inspected; no new numerical rules adopted by this review.

Keep campaign-length and attack-route direction: median52Cycles; average recorded53.17; all three routes used. Supply shortages slightly lower; no voluntary self-induced deficit entries. Trait parity remains unresolved (3–18 confirmed wins per36), with the unresolved200Cyclecase not counted as a win.

Before prescribing more trait buffs, correct two demonstrated bot faults: garrison transfers repeatedly undo themselves and can suppress fleet creation; defensive projects are valued as completed protection despite being unlikely to survive their Build stages. A five-stage Network selected against83.5% estimated immediate capture risk was destroyed nextCycle. Add explicit permanent-defence value to Consolidation's existing economic comparison. These are controller recommendations, not restrictions on player actions or changes to Integrity rules.

Grand Shipyard now has36active completions from47starts; Salvage7from45, with99victorious ground reward opportunities. Fortification Network0from39, and nine constructions still unpurchased; their campaign balance cannot be marked resolved. Keep approved numerical candidates pending the narrow corrections; no blanket nerfs, no automatic new batch, no timer. Historical campaign and source rules remain unchanged.

# Campaign design notes — 15 September 2026

## 27 September 2026 — approved trait/construction candidate implemented and comparison started

Implemented the approved three trait buffs and construction candidates in construction-trait-qualification-20260927, preserving the campaign and earlier frozen rules. Qualification_Report_2026-09-27.md describes the exact changes.397regressions passed;three distinct saved states plusfive designed situations assessed without mutation;four paired pilot games produced1,874replay-validated orders. A Network completion/preview validation issue for later owners was caught in pilots and fixed. Existing failure logs remain. Pilot durations55/32control and33/32candidate are qualification evidence, not balance conclusions.

Purchasing coverage is shared by both arms, with no forced build quotas. Pilots now naturally buy previously unused Cruisers, Scouts and System Defence Stations. Broader construction valuation remains heuristic, so inspect actual choices/completion/use before interpreting low purchase frequency as poor balance. The9-Supply Grand Yard is a Minor profile with3/6Integrity; the Major Salvage Wing candidate retains25-Supply/five-action cost while rewarding participating victorious ground assaults. Equal-budget arithmetic was compared with old yard costs and cheaper naval-only Salvage, including action/slot/upkeep caveats.

The new study is144pairs/288freshgames,2workers,balanced36appearances/trait/arm,12perseat,18permapfamily,and6–7encounterswitheachothertrait. Six general strategies each appear5times pertrait;trait-aware strategy6times. Numerical trait and construction changes are a combined package, so wins are not attributable to traits alone. Expected1.5–3hours;no recurring reminders. Root source draft and suspended Dessica remain unchanged pending evidence and campaign-release preparation.

## 27 September 2026 — trait approval and unpurchased construction inspection

Approved for the next candidate: Void Supremacy retains its expansion perk and waives ordinary fleet Supply upkeep; Fleet Endurance retains recovery and waives ordinary fleet Manpower upkeep; Fortification Experts retains free Defend/tier+2 restoration and gains 3 Supply after Defend, respecting deficit income locks and the one Faction Action. These are approved, not yet implemented in the frozen simulator or source draft.

The requested construction inspection covers every one of the fourteen profiles never started in the 144 latest candidate games. All fourteen lack direct purchase valuation. A saved-order replay of twelve selected campaigns (9,037 orders; 1,848 Construction decisions) found legal and fundable opportunities for all fourteen, so absence cannot be attributed solely to unlocks or affordability. The report is operational-correction-20260927/Unpurchased_Constructions_Inspection_2026-09-27.md, with individual assessments and evidence.

Priority findings: planetary regeneration and Landing Zones deactivate when host damage lowers their Integrity, while construction Repair requires a full host. Fortification Network increases maximum but not current defence, and one hit can deactivate and remove the capacity. These interactions need targeted correction. Grand Shipyard and Salvage Wing have weak observed economics: seven median fleets created per faction across a whole campaign; one median naval victory. A 25-Supply Salvage Wing requires nine equipped-fleet victories after completion to repay Supply alone; only three of 396 non-Industrial faction appearances had nine naval wins anywhere in their entire campaign.

Recommended construction candidates remain UNAPPROVED: retain completed base regeneration/transfer permission at positive Integrity; retain completed Network capacity until destruction and grant its added current defence on completion; compare cheaper Grand Yard construction and broader Salvage Wing earning conditions in saved, equal-budget situations. Do not indiscriminately buff Bunkers, shields or System Defence, whose effects can already be substantial. Give all profiles fair completion-aware valuation and assess Garrison Transfer, which bots never used. No forced build quotas, no claim that every construction must have equal purchase frequency, and no human Soulstorm win-rate inference. No new campaigns or publication during this inspection.

## 27 September 2026 — full operational and trait inspections complete

The comparison completed 144 new games against 144 exactly reused controls, with zero errors. Full inspection covers 288 traces, 5,065 construction histories, 1,264 deficit entries, 864 faction appearances and 8,286 independently replayed orders in 11 selected campaigns. Reports are in operational-correction-20260927: Full_Inspection_2026-09-27.md, Trait_Inspection_2026-09-27.md and Notes_Disposition_2026-09-27.md.

Retain the three controller corrections. Maximum duration fell from 187 to 95 Cycles, median duration from 53 to 51, and bombardment use rose from 486 to 842. Supply-deficit exposure worsened from 3.22% to 5.39% despite lower spending; enemy attacks triggered 77 of the 84 extra Supply entries. Actual Logistics Supply also fell. No voluntary self-order deficit was observed. Current deficit punishment and route rules remain.

Trait results require both focal and other-role context. Successes across all 36 appearances: Efficient 21, Salvagers 19, Martial 16, Mobile 13, Industrial 13, Siege 12, War 12, Dread 12, Swift 9, Endurance 7, Fortification 6, Void 4. These have unequal seat and strategy exposure; they are not a qualified 36-focal-case sample. Void, Endurance and Fortification are the priority buff candidates. Industrial's focal 1/12 is not representative of its 13/36 overall.

Proposals, not adopted: waive ordinary-fleet Supply upkeep for Void; waive ordinary-fleet Manpower upkeep for Endurance; let Fortification's Defend also grant 3 Supply while retaining its Faction Action cost and existing benefits. Deficit locks remain. Hold the other nine traits. Test a fresh, balanced 144-pair schedule across seats, maps and strategies, assessing the whole package rather than trait wins alone. No rules, batch, timers or publication were initiated by this inspection. Fourteen construction profiles remain strategically unexercised in this sample; passing mechanical checks do not establish competitive balance.

## 27 September 2026 — approved controller corrections and bounded comparison

Following the completed block1 inspection, the creator approved proceeding. Three isolated bot corrections are implemented: subtract Manpower upkeep in resource forecasts, evaluate local ground/bombardment opportunities despite a remote strategic target, and coordinate safe affordable restoration of useful unfinished fleet-construction hosts. No campaign numerical rule changed.

Qualification passed376 regression tests and6edge checks. Five saved games replayed6,671 original orders without divergence;255 saved choices inspected,17 changed legally. The long-war Cycle65 position now restores one builder and assaults locally with other fleets. A delayed-builder Cycle10 position now withdraws toward a yard. Two fresh pilots replayed1,453 orders and completed54/51Cycles. These checks establish concrete correction behavior, not final balance.

A bounded paired comparison began15:15Sydney:144 NEW corrected games against144 exactly reused prior candidate games. Same maps, policies, seeds and trait assignments; all new games independently replay-validated. Reuse saves repeating the control half; it is neither fresh holdout evidence nor extra trait sample size. Each trait retains12 focal appearances per arm. Root rules/draft, earlier studies and suspended Dessica preserved.

Assess the complete package after completion: resource shortages, war routes, campaign lengths, construction activation/use/interruption and Minor encounters as well as traits. Remaining disparities may require rule changes; this is not an open-ended demand for perfect bots. See operational-correction-20260927/Correction_Qualification_2026-09-27.md and Study_Plan.md. No timers or external publication.

Recorded 2026-09-15, Australia/Sydney. Source: Notes on Meta Campaign.txt. Review backlog, not a balance patch.

## Dessica suspension

Suspended at Cycle 21 after the Korps captured Corvid and finished its turn. Next would be Vior’la; no battle is pending. Resources: Korps 9/29, Vior’la 16/36, Cerberus 19/27. Opening event and Logistics already occurred. Preserve state/history; restarting or retirement remains undecided. No more turns or rolls until resumed.

## Directions incorporated into source v0.1

20/20 Subsector starts, not retroactive; separate Major/Minor role and Independent Alignment; fixed Subsector raider; narrative without mechanics followed by action tables; advisor recommendations versus commander declarations; versioned templates and control handover; GM publication/palette procedures and personnel/succession tracking. Lifespan profiles and Sector mechanics still need design.

## Issue register

| ID | Topic | Proposal/question | Status |
|---|---|---|---|
| B01 | Construction concentration | One per planet; encourage spread/upgrades; define mobile/system exceptions | Proposed |
| B02 | Orbital ground-attack contest | Losses in orbit; compare with Fleet Battle initiation cost | Open |
| B03 | Fleet battle versus ground-first | Make both credible strategic choices | Open |
| B04 | Economy | Meaningful spending swings, savings, interrupted projects and snowballing | Open |
| B05 | Manpower | Improve usefulness without automatically nerfing Supply | Open |
| B06 | Alignment/Sector | Independent requires pacts; subordinates and Sector roster transfer | Terminology adopted in source; Sector deferred |
| B07 | System generation | Weighted system-size/holding presets; Dessica as example | Pending design; no table approved |
| B08 | Minor strength | Consider halving fleets; exceptional prize factions with Capital worlds | Proposed |
| B09 | Minor economy | Holdings/tier-based faction resources rather than isolated worlds | Proposed |
| B10 | Combat randomness | Review player fleet combat and AI resolution | Open |
| B11 | Construction strategy | Credible alternatives to economy-first | Open |
| B12 | Traits | Compare situational/compounding; prefer strengthening weaker fun options | Testing pending |
| B13 | Bombardment | Higher costs/downsides to keep ground-first credible | Proposed |
| B14 | Planet Fall choices | GM for Minor; Major choice ownership or randomisation | Existing Minor ruling retained; alternatives pending |
| B15 | Raid identity | Fixed at Subsector setup | Adopted source direction |
| B16 | Events/travel | Balance events; consider delayed travel | Proposed |
| B17 | Alignment constructions | Warp resilience, Chaos/Necron options and fair access | Proposed |
| B18 | Personnel/time | Ages, successors, local/Sector clocks, trait continuity | Framework adopted; lifespans unresolved |
| B19 | Simulation quality | Multiple policies, uncertainty, sensitivity, meaningful choices | 216-game integrated baseline completed; policy limits and targeted gaps documented |
| B22 | Periodic construction timing | Test system-station damage-before-repair baseline against alternative timing before recommending station balance | Added 16 September 2026; source does not specify fine ordering |
| B21 | Defensive commitment timing | Automatic defender commitment can trigger an irreversible deficit before Planet Fall replaces that cost; review delayed net settlement versus current immediate entry | Added 16 September 2026; user directed preserving current baseline for testing |
| B20 | Mod subproject | Compatible kitbashed units/factions, animation and Army Painter support | Separate future work; no assets changed |

Suggested review sequence: terminology → economy/Manpower → Minor resistance → combat → construction/traits → generation/events → personnel/Sector. This is a recommendation, not an approved redesign.

## Briefing provenance and stale data

The three historical briefings informed voice, doctrine and role templates. Their Cycle 1 and 10/10 values are obsolete. Cerberus's Biomass Reclamation conflicts with the current Hive Ship trait; the Star-Blessed cult was retconned. The player-as-referee description is superseded by the current GM workflow. None of those stale mechanics is imported as current or new-campaign state. Their voices are examples, not mandatory styles for every faction.

## Original notes — verbatim

The following discussion is preserved as supplied. Tentative alternatives are not adopted merely by appearing here.

Perhaps we limit constructions to one per planet to force spread. Even though there is the ability to upgrade planets and build 
stations there is never any strategic reason to do so. There is also no tactical reason to not only build on your capitl at least
for economic buildings as the major faction capitals are the only 12 defense Planets/Stations/Massive Planet Scale Ships. It also
encourages Construction Upgrades instead of repeating Constructions across Planets.

Start at 20 Supply and Manpower unless directed otherwise by Sectorwide Gameplay. Starting Subsector Battles to determine Sector
Roster will always start at 20 Supply and 20 Manpower.

Maybe add something for fleets contesting ground attacks in orbit. So a 5 strength fleet attacks a planet with a 5 strength enemy
fleet guarding that system. Since the fleets engage above orbit maybe they both lose a strength or something? Unsure how to 
balance properly with initating fleet battle costs

Ai seem to be always deciding fleet battle first and then ground assault. Never ground assault first. I would like to resolve this.
There should be pros and cons for both choices that allow for Roleplay Decision making without tactical deficit. 

Economy seems off, I would like both resource units to swing from the bottom to the top of the ranges via spending so you can save
for big construction projects that might hurt badly if they are interupted because at the moment it appears like everyone will
slowly gather more resources and follow a roaming baseline as he campaign progresses.

Supply are very strong which is fine but Manpower feels somewhat useless. I do not want to nerf Supply but I want both
resource units to be equally useful. Whether this comes from creating new uses for Manpower or imrproving yield of existing uses
I am unsure.

There is confusion in the text with Independent Factions because it is used for Minor Factions. We need to remove the mentions of
Independent when attached to a Minor Faction as you have Independent Factions on the Alignment Scale for Major factions who exist
separately to Imperium Factions, Chaos Factions, Etc. Independent Factions are inherently Independent and do not group together
like other Alignments unless pacts and deals are made via diplomacy or an Independent Faction creates a new Faction via Summon 
Allies to create a subservient faction whom they could also grant the subsector to in order to raise them to a Sector Level Ally
as the same alignment rules apply and take more precedence for Sector Wide Campaign Level. The entirity of the current Campaign
has been at Subsector Level, at least one to multiple Subsector Level Campaigns must be completed to generate the roster for 
Sector Level gameplay. Sector level gameplay needs to be fleshed out more but is not completely relevant right now to Subsector
fixes but will be relevant later.

We need a bunch of presets for system sizes and the planets within them so we can do a roll on a random table or something when
we are making new campaigns. Dessica should be a good example.

Minor Factions currently seem way too strong. They are supposed to function as bugs on the windshield of Major Factions.
Something for Major Factions to eat and gain resources while they prepare to take on other Major Factions. I think current 
Fleet Sizes seen at the start of the Dessica Campaign should be halved. I have the original Dessica Campaign document if we
need references but there is a considerable amount of outdated info that got patched and some of that was to do with fleets in
system. Perhaps we have one or two minor factions who retain the same fleet strength rules as we currently have and give them 
actual 12 defense capital planets. This makes them like prizes for the Major Factions to compete over and can leave bait to 
encourage over extending.

On Minor Factions one thought I have had would be to tie Minor Faction Supply to planets or stations controlled and what type/size
they are. That way each planet does not feel like it's own little isolated island.

Fleet Battles also need some balancing. Works in practise because I built it off the simple rolls I made for Ai to Ai combat but
it seems too random for me as a player, that randomness worked fine for background noise with Ai fighting each other but it is not
stimulating for me as a player. Perhaps both Fleet Battles and how we handle AI to Ai combat need to be looked at. 

I am unsure if this is part of the campaign or not but the ai seems to focus on economic construction heavily first and then move
to other construction types there doesn't feel like there is any room for roleplay because you have obvious correct choices instead
of a series of even choices that can vary depending on the playstyle of your faction.

Speaking of factions. Faction Traits. After playing as the Death Korps I am realising how badly the balanace appears to be broken
for faction traits. Some balancing simulations will tell if I am correct or just being salty. However the Tau and Tyranid Traits
seem vastly superior to mine as my trait is situational but the others have faction traits that give them access to immediate
snowballs. Now with faction traits I do not wish to nerf the stuff that works and is fun if we can avoid it. Just bring the weaker
stuff up to scale.

Orbital Bombardment should be more expensive or have some kind of extra downside as the Ai seem to always choose it as the option
first before ground assaults which means it is the statistically best option and we need room for Roleplay choices that are still
tactically compotent or at least in charater if they are not.

For situations like Planet Fall damage involving Minor Factions and which fleet takes what damage that is for the Game Master to 
decide. If it involves a Major Faction's Fleets then it is up to said Major Faction to decide. Or alternatively we could make 
planet fall damage a random chance where you run a randomiser script? That seems better now I think about it but I am unsure what
is best for overall balancing. That way we can save context by messaging another instance solely for the purpose of this choice
without going through a turn themselves.

Another thing, the Third Party Raider Faction should be established for the Subsector at Campaign start for clarity that way
it is easy to remember and you aren't swapping and changing with each battle.

Random Events need some work as well as balancing. One interesting idea for a random event however or maybe we add it to the existing
Warp Storm Affects could be delayed travel time?

I was thinking about giving certain alignments buildings. To be honest I cannot really think of any Factions outside Chaos and the
Necrons who justify this but something that allows them to bypass the negative events of a warp storm due to Chaos being, well Chaos
and the Necrons having alternative means of FTL and Blackstone. This means the other Alignments will likely need this as well.

Needs overall Polish and Balancing. I had Claude run several balancing Sims before the Dessica Campaign and said everything turned
out great. Part of the issues are due to my own direction but there is alot Claude missed mostly because it used simple simulations
and simple testing bots with simple strategies which has led to things like the massive over value of supply. Which I had allowed
but I was not made aware it was this bad and was told Manpower was still about 80% as effective as Supply which does not appear true.
I could be salty but I think the system would benefit greatly from balancing simulations on an extensive level. The concept for this
system is the War Games Perturabo played with his sons.

Faction Traits are tied to Commanders but if a Commander dies mid Campaign which Humans are prone to do in long Campaigns the
Successor must be the Faction Trait of the original. A Major Faction may choose to kill off their Commander or Support Staff for 
narrative reasons at any point in the campaign. Commander and Supporting Staff like advisors must have their lifespans tracked. They
must be replaced once they die of old age within the average death age of their species at the choosing of the Major Faction. The
Game Master should also be doing this for Minor Factions. Humans will usually suffer at least one Commander swap per Subsector
Campaign due to lifespan, however in universe medical treatment can extend this considerably. However on a Sector Scale Human
Commanders will swap with some frequency while Factions like Space Marines, Aeldari, Necrons, etc will retain their Commanders due to
longer lifespans but even they could perish from age depending on the total length of the campaign. This explains why a faction trait
does not change over time but the Commander does. I expect this to be fairly common given the Chronostrife and Subsectors all
operating on separate timescales with Sector level again being a separate time scale.

Once these changes are complete we need a blank version of the Document to use as Source Material for future campaigns so it contains
all system information but allows us to fill in our own campaign info into the framework. So we will copy the Dessica Campaign and
then wipe Dessica Specific Info from the copy to create the Source Document. We will also need a similar Source Document that
outlines faction briefings for both Commanders of other Rival Factions as well as the Advisor who serves whatever Faction I am 
playing and possibly something for if I decide to take over a different faction so the the ai now knows how to play the Commander
like the other Major Faction Instances are. This creates consistency between Campaign Updates if we can make confirmed changes to
the Source Documentation it will spread through all new iterations. With the briefings it should state that the narrative section
should not include meta terminology from the system and focus purely on the narrative. Then the Meta Information is presented
in the same box format as I have been using for the Dessica Campaign. Advisors present recommended actions and Major Faction 
Commanders present their actual actions. We also need to ensure any smaller rules such as not uploading to Github while waiting
for Player Battles to resolve in Soulstorm are recorded somewhere in the Source Documentation or perhaps we have a separate bit of
Documentation for the Game Master? Yeah we definently need an extra document for the Game Master because it should direct the game
master to help you pick the colours of each faction when you make them. I can provide images of the character creator so you know
how many colours to choose from and roughly where they sit on different models with different changes. Obviously I am not going to
show you all models and this could lead to some bad designs but the player can retcon these choices. It is important however for
each faction to have their own thematically appropraite and cool looking color palette.

Now these are not exactly system notes but a Sub Project to keep in mind. I would like to experiment with using existing models and
animations from the Unification Mod and Soulstorm Base Game to create new playable factions like a Tyranid Cult instead of actual
Tyranids as well as making some changes to existing faction unit line ups. Kit Bashing or using other models from other 40k games
is the best way to do this to ensure accuracy as they need to fit within the army painter system and be able to use animations 
correctly. Best way to do this might be to restrict ourselves to assets from Soulstorm, Winter Assault, Dark Crusade and their 
respective mods as we know those models and animations will work and for anything custom we can kitbash existing models from the
listed material.

## Simulation work begun — 15 September 2026

Military-grade scope confirmed for both resources; Supply costs must remain for fleet building materials. Added a reproducible frontier/diagnostic laboratory, ledger tests and explicit coverage limits. This is not a full-game balance certification. See Balance_Simulation_Methods.md and Balance_Simulation_Report.md. No fleet-cost candidate adopted.

## Simulation continuation — 15 September 2026

Shared-Major integration tests and reproducible traces are now available. This is not an adopted rebalance. Read Simulation_Development_Handover.md to resume development; it is included in the source library and simulation bundle. Supply still represents military materials and all experimental crew-cost variants retain Supply expenditure.


## Review update — 16 September 2026

**Approved ruling:** Establish New Capital takes priority over Emergency Rationing. Deficit resources stay locked at zero and their recovery progress is preserved during capital establishment. The next available Faction Action after establishment addresses remaining rationing. No extra Faction Action is granted. Added to Source_Rules.md; suspended Dessica remains unchanged.

**Simulation correction:** The first shared-Major prototype omitted Planet Fall resource penalties. Those historical results are unsuitable for economic conclusions. The engine now applies them and separates a captured capital-tier holding from an established capital's non-transferable built-in shipyard. Replacement capital actions and mobile-capital destruction are tested.

**Planner progress:** Bounded future-turn rollouts include opponent responses, privately sampled future events and delayed investment choices. The comparison shows that fleet creation can disappear under immediate-value bots and reappear under lookahead. This is a modelling warning relevant to B19, not evidence for adopting any balance proposal.

## Campaign-duration balance target — 16 September 2026

The user clarified that average campaign duration should be approximately 50–100 Cycles, with natural swing and some shorter outliers. Do not balance toward a mandatory100-Cycle minimum. Measure the distribution of actual endings and distinguish unfinished/censored runs from completed campaigns; extend observation beyond100 where necessary. Exact simulation victory/ending criterion is pending clarification. Early elimination alone is not a bot or rules failure. This records a design target, not an adopted rules change.


## Bot stagnation investigation — 16 September 2026

Do not rebalance the campaign economy to compensate for poor bot coordination. Nine additional 100-Cycle diagnostics found that a target-focused controller with a funded operational budget gained 8/7/8 holdings across three combat seeds where the original bot gained no territory (finishing with 1/0/1 holdings). Tactics-only and refusing-ceasefires-only variants were eliminated in the original seed; resupply-only did not expand. See Stagnation_Investigation_Report.md. The diagnostic fifteen-capacity force budget and 65% attack threshold are test settings, NOT proposed campaign rules. Production bot qualification remains outstanding; 174 regression tests pass. Average campaign-duration target remains approximately 50–100 Cycles with shorter outliers. Dessica remains suspended.


## Production bot and trait qualification — 17 September 2026

All 12 traits now rotate independently across six strategies and three turn positions in a 432-game, 100-Cycle-per-game qualification matrix. The production controller accounts for multi-turn operations, combat effects, resources, repairs and diplomacy; a free-expansion policy error for Void Supremacy was corrected. 210 regression checks pass. Current readiness and measured evidence are in Simulation_Readiness_Report.md and Trait_Qualification_Report.md; earlier stagnation reports remain historical.

This qualifies scoped baseline comparisons, not a rebalance. Small-map duration must not be used as a representative campaign average; the two ten-system checks reached control at 52/68. Use more seeds and representative maps for the 50-100 Cycle target. Siege Doctrine and Dread Reputation have player/AI distinctions, so AI-only rankings cannot establish their full value in player games. Less-used construction/action strategies require targeted testing before recommendations about them. No numerical change has been adopted; Dessica stays suspended.

## Integrated balance review begun — 17 September 2026

The user directed a cohesive review of the full notes rather than sequential adoption of isolated changes. A common 216-game ten-system baseline is being collected for economy, construction, Minor resistance, combat choices, traits and events together. Candidate packages will be compared on matched scenarios, with interaction checks. Integrated_Balance_Review.md maps every issue to the shared review or identifies items requiring separate design. No balance changes adopted; sample collection is in progress.


## Section-by-section review — 17 September 2026

Campaign_Notes_Review_2026-09-17.md now reviews B01–B22 and the source/briefing/GM requests. It combines the 216-game baseline with construction-choice audits and exact combat/rounding calculations. It proposes a connected v0.2-A package and a trait variant, rather than adopting isolated fixes. The raw original notes remain unchanged. Proposed rules have NOT been applied to Source_Rules.md or Dessica. See Integrated_Notes_Evidence.json and Balance_Microtests_20260917.json for reproducible measurements.


All five formerly unfinished cases reached full control: 102, 108, 111, 115 and 169 Cycles. Each 200-Cycle extension reproduced its original first 100 Cycles and orders exactly, then passed public replay. Including these endings, all 216 campaigns reached full control: mean 63.26, median 61, range 42–169. This is a complete duration distribution for this fixture, not all campaign maps.


## Creator corrections — 17 September 2026

The first v0.2 proposal was materially rejected. Campaign_Notes_Review_2026-09-17.md now records accepted designs, withdrawn ideas and open questions in the creator's point order. It supersedes prior recommendations, without overwriting the original playtest notes. Resource caps, finite naval damage ceiling, permanent Dread difficulty modifiers, sparse d6 systems and damage-only storm protection are withdrawn. Accepted designs are pending synchronized source-rule/simulator implementation, not already validated by the historical baseline. Mod development is parked.


## Concrete replacement proposals — 17 September 2026

The creator requested actual replacements rather than another restatement. Balance_Replacement_Proposal_2026-09-17.md supplies formulas, examples, attack choices, naval damage, traits, a complete d20 generation table and lore-supported all-alignment Warp Storm bypass. These are candidates, not silently adopted rules. Earlier accepted directions remain accepted for the next synchronized implementation. The underlying qualified engine and suspended Dessica ledger are unchanged.

Exact probability/setup checks are in Proposal_Checks_20260917.json; no full-campaign outcome is claimed for the new package. Sector work has now explicitly been TABLED by the creator while Subsector balance is resolved. The missing separate Sector document is not grounds to invent a replacement. Mod work remains tabled.

## Latest decisions — 17 September 2026, follow-up review

Accepted for the connected candidate: holding construction rules and upgrade continuity; Expand Fleet personnel cost; resource-based ground formula; shared Minor pools; naval formula; ground breakthrough and bombardment pricing for testing; Siege successful-assault bonus; Warp transit implementations. Fleet and system construction limits are NOT approved. Remove the merger restriction: absorbed constructions transfer.

System generation is now 2–4 total holdings (planets and stations combined), with a mean of 3: d20 1–5 gives 2, 6–15 gives 3, 16–20 gives 4. The updated proposal contains all twenty mixed profiles. A ten-system/three-Major map averages 30 holdings.

Pending candidates: double the whole derived resource pool of designated prize Minors (including a proposed persistent designation after Capital loss); Fortification retains normal Defend prices and +2 restoration, with one completed defensive construction Integrity repaired if the host reaches full defence; Dread replaces its old effect with defensive Build/Upgrade at 3 Supply per stage. The rejected flat 1/1 Defend and half-defence capture proposals must not be implemented. These trait replacements have arithmetic comparisons, not validated balance claims.

Mandatory evaluation: bombardment must have useful situations beyond being the only legal option at extreme Manpower shortage. Compare all three attack routes together. Exact generator and route-affordability checks pass, but no new full-campaign candidate run has occurred. Source_Rules.md and the qualified engine remain the historical baseline; Dessica stays suspended.

See [updated replacement package](Balance_Replacement_Proposal_2026-09-17.md).


## Revised testing completed — 17 September 2026

432 games and 386,978 orders replay-validated; 227 regression tests plus 6 edge checks. All 36 route audits and 100 player setups checked. See Revised_Balance_Testing_2026-09-17.md for complete findings and recovery provenance. Testing complete; website publication is being performed next. Dessica stays suspended at Cycle 21.

## Assessment and next priorities

The duration target is broadly met in this sample: 316/432 games (73.1%) finish in Cycles 50–100, 89 (20.6%) finish earlier and 27 (6.3%) later. Generated maps put 75.9% inside the target versus 70.4% on historical maps. The historical paired interval crosses zero, so this does not establish a duration improvement over baseline. All games finish by 200, but only 346/432 have full territorial control at the coalition endpoint. This remains a competitive-duration assessment, not a guarantee about clearing every Minor holding.

Bombardment remains used: 2,113 orders across 373/432 games. In the route audit, 103/149 bombardments had no affordable Ground Assault alternative; 46 did, including 10 with at least 65% modelled victory odds. It therefore has a viable niche, often when ground commitment is unavailable, with some use even when assault is attractive. Usage alone does not prove the pricing optimal. The 39,110 ground/mobile assault orders versus 5,239 naval orders contradict a universal fleet-first sequence, but aggregate counts cannot establish that every tactical situation gets the best choice. Preserve all three routes for further playtesting rather than declare bombardment obsolete.

Resource shortages remain consequential: 3,129 Emergency Ration actions. Supply was locked for 3.49%/2.92% of surviving faction-Cycles and Manpower for 2.40%/2.10% (matched/generated). Positive average stocks do not mean a struggling faction has adequate resources; the averages omit eliminated factions after elimination. No additional shortage penalty is justified solely by these aggregates.

All 12 traits were included. Across both arms, focal survivors were mobile 21/36; martial 18; efficient 16; salvagers 14; swift 13; war_economy and endurance 12 each; siege 11; void 9; dread and fortification 4 each; industrial 2. These are shared-block heuristic-bot observations, not independent trait win-rate estimates. Mobile and martial deserve scrutiny for strength; industrial, Dread and Fortification deserve scrutiny for weak payoff or poor bot use. Siege does not show dominance. The Fortification bonus repaired a construction only once across the entire sample: its new secondary effect is demonstrably rare under these bots, so it cannot presently be credited as a substantial counterweight. Audit trait-specific opportunities and bot decisions before choosing new numbers. Do not infer that the lower observed traits are equally weak for a human defender.

The next rules decision should address player formation scaling, alongside the weak defensive/construction trait payoff. Keep the implemented package available as a tested candidate; do not label it fully balanced or replace the preserved baseline silently. AI combat outcomes cannot predict human Soulstorm/Unification win rates. Sector gameplay and the mod project remain tabled.

## Execution recovery record

Matched case 208 initially hit a MemoryError while serializing a snapshot alongside other workers. It completed unchanged when retried alone: same seed, rules and fingerprint, 2,727 replay-validated orders. The original error and recovery record are included in the evidence. The final manifest elapsed_seconds describes cached-result consolidation, not the total study runtime; the main batch took about 4,643 seconds plus the isolated retry and subsequent audits.

## Trait candidate and formation series approved for testing — 17 September 2026

See trait-candidate-20260917/Trait_Revision_Rules_2026-09-17.md. New trait buffs are test candidates, not validated balance. User accepts prior campaign-length and attack-route changes. Replace proportional compression with reported winning survivors and finite reserves; raid rounds have equal three-team main sides and a single nonrespawning raider. Full implementation tests pass; new864-game comparison planned, including independent holdout.

## Trait study and audit COMPLETE — 18 September 2026

864 trials,767238 validated orders;3 unresolved at200,zero execution errors.72 audit replays complete. Read Trait_Balance_Results_2026-09-18.md. Development/holdout trait spreads13/18 exceed tolerance5.603/864 finish50–100. Audited Industrial savings358Supply; Fortification261Supply+261Manpower; Void193 extra strength. Siege defeat captures358 across full sample. No new balancing changes adopted. Local completion monitor should be paused after notification; publication remains blocked. Do not rerun study. Baseline/R2/Dessica preserved.


## 18 September 2026 — Whole-system bot qualification
Rules remain frozen. A new isolated controller compares broader action choices and economic payback. 250 regression tests and an initial six-game pilot pass; this does not establish balanced traits or qualified strategic play. A36-pair/72-game controller comparison is running. See bot-candidate-20260918/Bot_Development_2026-09-18.md. Diplomacy and detailed opportunity-based audits remain outstanding. Dessica remains suspended.

## 18 September 2026 — Early bot checkpoint
Stopped controller screen after first pair exposed sustained fleetless stagnation despite abundant resources. Fixed consideration of distinct Faction Actions, safe-yard rebuilding when fleetless, and expansion of a lone weak fleet before departure without local combat. Rules unchanged. Focused sequence restores1->3->5; full competence not yet qualified. Preserved report: bot-recovery-20260918/Bot_Recovery_Checkpoint_2026-09-18.md. No full batch or timer running.


## Approved connected rules package and paired testing — 19 September 2026
User approved Industrial fast initial Build, Swift creation at5, Siege ground-cost reduction, and finally Fortification free Defend. Rejected Fortification construction discount/eligibility categories and two-holding Defend. Final candidate: zero Supply/Manpower Defend, existing tier+2 restoration and Defended, one Faction Action, no incidental construction repair. Industrial new project2Integrity/3Supply, subsequent stages1/3; upgrades/repairs do not accelerate. Swift5 starting strength, no creation-Cycle action. Siege max(1,tier-1) base ground Supply, Dread additional afterward; no changed defeat damage/bombardment. Prior accepted routes/duration/construction rules retained. Historical root engine and Dessica remain unchanged.

Isolated balance-package-20260919/control and candidate copied from latest bot-plan-study. Found old engine early-return forced ration-only during deficits, contrary to user's existing ruling allowing other affordable actions. Corrected in BOTH arms, retaining blocked Reinforce/Muster for corresponding locked resource and replacement-capital priority. Candidate cost estimate uses new Siege cost; no bot strategic threshold tuning. Old expected test totals updated only for approved mechanics. Control277 regression+6edge, candidate283 regression+6edge all pass.

912-case study launched via hidden Python PID19764, three concurrent workers. 864 primary campaigns =2rulepackages x12traits x6policies x3seats x2maptypes. New seed blocks491900+, fixed within trait comparisons and paired packages. Maximum200Cycles, stop on singleMajorcoalition; censor retained, not fullterritory conquest. 48 additional30Cycle checks =2packages x12traits x2policies, focaldeliberative othersoperational, generatedmaps, forcepriorityFalse/readyvalueTrue. Six established strategies are frozen; no claim optimal bots. All case orders independently replayverified before saving; frozen inputs, compressed traces, errors retained, cached successfulcases reusable. Do not duplicate runner or modify pinned code.

Progress: balance-package-20260919/progress.txt, errors.txt, manifest.json, results.json. Main runner study.py auto-runs analyse.py after finishing; Results.md and paired-differences.json are preliminary summaries needing human interpretation and representative trace review for construction payback, defensive loops, attackalternatives and resource expenditure. Deficit exposure, Dread payments, Siege defeatcaptures and buildprofiles saved. Shared seeds are blocks, not independentreplicates. Planner30Cyclechecks do not measure game length; AI doesnot predict humanSoulstorm winrates. No timer, automation, GitHubupload, or campaignadvance. Userrequested owncheckback estimate. Do not resume bot outcomechasing; only fix reproducible implementation defects.


## Approved bookkeeping ruling — 20 September 2026
Each Cycle begins with Phase 0, resolved globally once before any faction turn:
1. Constructions: resolve due automatic construction effects.
2. Logistics: on a Logistics Cycle, resolve Logistics, including eligible construction income, once.
3. Events: roll and resolve the Cycle event.
Construction income is paid in step2, not twice. This establishes the category order; competing construction damage/repair effects within step1 still need one simultaneous-resolution convention. No frozen test inputs or running cases changed. Automatic defensive battle expenditure remains a separate combat-timing issue, not a Phase0 effect.
Soulstorm global difficulty/allied-AI issue deferred at creator request.


## Defensive expenditure ruling — 20 September 2026
Creator confirmed automatic defensive expenditure settles on the attackers turn, after the attack. Apply the final defensive cost or Planet Fall replacement once, then deficit entry; no temporary resource debit causing deficit before resolution. Record as approved future engine change; current frozen test batch unchanged. The resource totals used to calculate the combat roll remain a separate calculation and must not be silently changed by this timing clarification.


## Read-only notes assessment — 20 September 2026
Completed 864-summary/48-trace sequential audit without new tests. See balance-package-20260919/Notes_Evidence_Review_2026-09-20.md and corresponding JSON. Real resource volatility; MinorDepot8 vs MajorForge5 Logistics payouts for Supply repayment; construction preference confounds observed economy-first. No unapproved mechanics changed. Running planners untouched.


## Next experiment staged — 20 September 2026
Minorconstruction3Supply/stage,Major5,Industrialminus2minimum1 approved for nextcomparison. Fourarms staged in construction-strategy-prepared-20260920; see Preparation_Handover.md. No newtestprocess launched; existingstudy901/912at17:23. Newcode awaits regressionupdates/validationaftercurrentstudy, launchgated. Traitcontroller is existingpolicy matching,not claim optimizedbots. Proposed1728games withfreshseeds; no timer/autostart.


## Three construction/strategy batches complete — 21 September 2026
All1728uniquecases saved,1579864replayedorders. Allthreev2stage manifests complete; batch1twofailed none-trait cases repaired,originalfailureevidence retained. No run active or further launch. Aggregate report metadata corrected to read v2stage manifests ratherthan staleoriginalmanifest. Results.md at construction-strategy-prepared-20260920. Minor starts general3394->3995(+17.7%),trait3883->4641(+19.5%);Major2512->2592,2683->2764. Rationgeneral2841->2075,trait2170->1913. MedianCyclesgeneral63->62,trait60->60;50–100general302->292/432,trait295->273/432. Pricecut improvesaccess butnotdurationdistribution. Traitmapping notuniversalimprovement: cheaperSwift17generalvs7trait,Industrial15vs7,Endurance14vs6;Mobile8vs14,Dread4vs8. These are matchedpolicycomparisons,notoptimaltraitpower. CandidateTrait spread11,stillabove5. OrdinaryMinorDepot/Training starts absent inallfourarms; rankedconstructionpreferences confoundchoice. Consolidationgeneral48->0,trait25->0;VoidStationsnone. Do notdeclarewholecataloguebalanced; no automaticrevertornewbuff. Recommendretainlowerpriceprovisionally,do notpromotefixedtraitmapping,reviewMinorincomeversusMajorandholding-expansionopportunitycost usingrulearithmetic. No humanSoulstormwinrateclaim.


## New approved package prepared — 21 September 2026
See economy-timing-study-20260921/Study_Handover.md. Twoarms,336gamesfirststage; newMinorincome/developmentcosts/Phase0/defensivesettlement,randomizedfixedstrategiesincludingtraitoption,andobservationalmeasurements. Control291/candidate295regression+6edgeeach pass;pilotpendingbeforelaunch. No rootengine orDessica changes. No autostartlaterstages.


## Economy/timing firststage complete — 22 September 2026
336cases,318484replayedorders,0errors,1h51m. See economy-timing-study-20260921/Stage_1_Results_2026-09-22.md. Median67botharms;target119vs116/168. Consolidation18starts12complete6zero;VoidStation1startdestroyed;noMinorDepot/Trainingstarts,soincomeproposalnotstrategicallyexercised. Sameforcelegalalternativerouteobserved23.4%bombard,22.3%ground. Mosttraitsuccessesunchangedoutof14. Newtelemetry analysedsequentially;no newtestsorstage launched.


## Creator clarification — 23 September 2026: replacement Capitals
All planets and stations are eligible. Establish New Capital requires full12/12, retains accelerated cost-free action and priority over rationing. No remaining planet/station/MobileCapital means Subsector elimination and destruction of stranded fleets. InitialSectorroster comprisesSubsectorwinners; creator may narratively reintroduce others in latercampaigns. Sector-scale expulsion rulesdeferred. Implemented in isolated capital-recovery-fix-20260923; historicalstudyinputs unchanged.305regression+6edge checks passed; savedstation-onlycase now legallyestablishes thenrations. No fullbatchrun.

## 26 September 2026 — Final playability comparison in progress

Inspection found a diplomacy mismatch: trait-led bots used the trait strategy for military orders but a legacy fallback for accepting ceasefires. This could maintain peace indefinitely despite readiness to fight. The correction is common to both new comparison arms. Two previously unresolved saved positions finished after four and nine additional diagnostic Cycles; these used fresh random sequences and are not new paired balance results.

The authorised experimental package retains Efficient 6 and Major economic constructions 7/14. It tests Swift full restoration through Expand Fleet at normal costs, retaining full-strength creation, and Endurance +2 recovery each Cycle instead of only Logistics Cycles. Recovery does not restore construction Integrity or destroyed fleets. These buffs address exercised but weak traits; they are candidates for testing, not a declaration of equal power.

336 paired games launched locally in playability-confirmation-20260926, covering all traits and strategy options on both map types. Review all campaign systems, not merely trait survival. No automatic follow-on batch. After this confirmation, aim to consolidate a playable rules freeze and use actual campaign play to investigate remaining uncertainty. Human Soulstorm difficulty remains deferred. Suspended Dessica is unchanged.

## 26 September 2026 — Confirmation inspection completed

Saved records confirm Swift's revised expansion delivered 144 extra Fleet Strength across 115 orders; Endurance's actual restoration increased 46.3%, chiefly through recovery outside Logistics Cycles. Neither improved focal survival in this sample. Keep the buffs provisionally for human play, without claiming trait parity or escalating them again automatically.

The one candidate campaign still active at Cycle 200 is identical in both arms, contains neither changed trait, and recorded 11 captures during its final 21 Cycles. This is prolonged warfare rather than an inactivity deadlock. Preserve it as a watch item, not grounds for an immediate Fortification nerf.

Recommendation: retain the diplomacy correction, consolidate a playable rules freeze and resume campaign play before another broad simulation batch. Global Soulstorm difficulty and remaining trait uncertainty stay explicit. Full findings: playability-confirmation-20260926/Inspection_Recommendations_2026-09-26.md. No new simulations were run for this inspection.

## Full notes reconciliation — 26 September 2026

Campaign_Notes_Reconciliation_2026-09-26.md reviews every B01–B22 item and separates implemented mechanics from unresolved balance evidence. It supersedes the recommendation to return to play merely because the final batch ran cleanly. Trait parity, catalogue/development value, same-position route/siege decisions, Minor ease and event/resource attribution remain open. Latest candidate started 16/33 construction profiles; 17 unstarted profiles cannot be declared balanced. Economic utility is explicitly modelled for six profiles; military choices retain heuristic preferences. Root source contains stale Phase0, defensive-settlement, allocation, raid, trait and cost text and needs coherent consolidation. No new rules adopted or tests launched. Deferred Soulstorm difficulty, Sector and mod work remain deferred. Preserve original notes/history and Dessica.

## 26 September 2026 — Construction amendments and targeted siege checks

Implemented the authorised Carrier10/20 ground strength, Siege Platform3/6 damage, Regenerative Fortifications3/6 eligible recovery and Minor Landing Zones in isolated construction-siege-candidate-20260926. No change to published source or Dessica. The bot now prioritises active system fire and remembers failed siege progress. Targeted checks verify costs, commitments, upgrade/Integrity behaviour, Mobile Capital recovery and transferred fleet constructions.

Saved-position comparison improved station targeting but did not resolve the siege: after twelve diagnostic Cycles the retained correction had22Fleet Strength and station8Integrity, versus control3Fleet Strength/station10. A stricter arrival rule performed worse and was reverted with evidence retained. A longer batch is not yet justified; the outstanding issue is a feasible coordinated suppression plan versus ongoing defender repair. Detailed costs/trade-offs in construction-siege-candidate-20260926/Targeted_Results_2026-09-26.md. This updates the backlog; it does not declare trait or catalogue balance complete.


## Focused siege comparison completed — 26 September 2026

Completed siege-plan-comparison-20260926: 12 eighteen-Cycle continuations from the saved generated20 Cycle200 position, four plans across three fresh seeds; 2,683 orders replay-validated, all twelve saved traces separately audited. Two reassessment regressions passed. No full campaign batch or timer. See Results_2026-09-26.md in that directory, decision-audit.json and station-construction-interaction.json.

The adaptive baseline finishes with 24–28 holdings and flank pressure with 27–28, versus 8–9 for rigid station suppression and 9–12 for rigid Capital assault. No Capital capture within the window. The adaptive baseline disables the target station in one seed: six strikes reduce Integrity10 to4, then3, while the defender spends actions elsewhere. Fixed assembly allows enemy territorial recovery and fails to reassess returning defenders; production suppression already rejects the hopeless guarded attack. Retain r1; no new production policy threshold or additional combat rule adopted.

Construction interaction is the next concrete concern: automatic station fire disables base Carrier/Siege bonuses before assault; upgraded versions retain their base effect, while Flagship capacity persists. Proposed for creator review only: completed Fleet Constructions retain base effects while Integrity>0, upgraded effects still require full upgraded Integrity; incomplete and planetary/system activation rules remain unchanged. This changes the creator's existing activation rule and has NOT been implemented. Do not silently treat it as approved. No claim the siege, whole catalogue or trait parity is solved. Root baseline, prior evidence and suspended Dessica remain unchanged. No testing process from this comparison remains running.


## Fleet Construction activation approved and implemented — 26 September 2026

User approved completed Fleet Constructions retaining base effects above zero Integrity; upgraded effects require full upgraded Integrity. Implemented in fleet-integrity-candidate-20260926. Canonical dated amendment: Fleet_Construction_Integrity_2026-09-26.md. Planetary/System effects, incomplete projects, permanent strength conversions and damaged-upgrade eligibility preserved. All eleven Fleet profiles are included, including Scout; Warp Storm restrictions remain.

336 regression tests + six edge checks pass. Controlled station-fire checks: base Carrier ground3->13 and winning damage1->3; base Siege Platform winning damage1->4. One saved eighteen-Cycle continuation independently replay-validates283orders and exactly matches previous baseline history/actions; it does not establish siege resolution or broad balance. See candidate Results_2026-09-26.md. No full batch or timer. Previous studies and Dessica untouched; local amendment not yet published. The recommendation is now APPROVED, superseding the previous handover's pending status. No process remains running from this work.


## Construction-choice comparison launched — 26 September 2026, 20:47 Sydney

User authorised purchasing corrections, saved checks and one bounded comparison batch. Directory construction-choice-study-20260926; runner PID29100 (also runner.pid). Three workers,336 paired games, no timer/reminder or automatic next stage. Both arms use approved fleet-integrity-candidate rules; candidate changes construction purchasing only. Estimated2–3hours; user advised check around23:45Sydney. Read stage-0-manifest.json/progress.txt/stderr.txt; do not launch a duplicate. Confirmed running with2pilot cases/2421verified orders/zero errors.

Candidate adds construction_choice.py and integrates its estimates for Carrier, Siege Platform, Bombardment Bay, Flagship and forward shipyards. Includes financing, reserved resources, build time, ordinary fleet replacement/Manpower/upkeep/opportunity costs, surviving effects under station fire and actual local repair demand. Repair priority and existing defensive-emergency choices are preserved. Construction under automatic fire is rejected. Estimates remain heuristics; other construction profiles retain existing evaluators. No claim all catalogue choices are optimal or qualified.

Validation:343candidate regressions,336control,6edge checks. Three saved final positions/four surviving faction decisions inspected:020 safe fleet60 Siege investment scores positive but a concurrent home incursion preserves the existing emergency upgrade10 response; unsafe fleet59 is excluded.047 chooses local shipyard;063 retains RepairTender. First candidate pilot before final emergency guard archived in preflight-before-emergency-guard and excluded from batch. Final candidate matched000=62Cycles/807verifiedorders;control generated020=111Cycles/1614orders. Both pilot input hashes checked against final code; retained as batch cases. One wrong-working-directory test invocation is retained; correct-directory full suites passed. Pilot metadata supplemented with final construction inventory, without changing traces/outcomes.

Study_Plan.md and saved-purchase-checks.json contain scope/limitations. Runner automatically writes comparison-summary.json through analyse_results.py when all cases finish; it does not launch another stage. Assess whole package:50–100Cycle distribution/censoring, resource exposures, three routes, starts/final construction status, all12 focal traits and paired outliers. Final inventory is not lifetime uptime; distinguish censored survival from winning. No human Soulstorm prediction. Root baseline, prior evidence and suspended Dessica untouched; no publication performed.


## 27 September 2026 — approved integrated decision comparison

All eight recommendation groups in Full_Recommendations_2026-09-27.md approved. Isolated planning/valuation corrections implemented; current rule values retained. Candidate360regressions+6edges,control343;3,386saved orders replayed with160decision checks. Catalogue33base-build paths,200player setups and54short route diagnostics checked with stated limitations. The current rules draft and source templates are consolidated locally; historical baseline and DessicaCycle21 remain unchanged. Block1 of the864-game paired comparison started atapproximately03:16Sydney:288games,threeworkers,expected2–3hours,no reminders or automatic next block. Full findings await completion and inspection; no claim of trait parity or human Soulstorm prediction. See integrated-decision-study-20260927/Preparation_Report.md and Study_Plan.md. Nothing published externally.

## Full block 1 inspection completed — 27 September 2026
Study: integrated-decision-study-20260927. All 288 games / 226,362 replay-validated orders completed, no errors. No further block running. Full report: integrated-decision-study-20260927/Full_Inspection_2026-09-27.md.
Inspection checked all 288 trace hashes/final states/order counts and frozen inputs, 5,646 project histories, 1,224 deficit entries, and replayed 9,464 orders across eight selected games with 419 saved construction positions. A separate Cycle65 saved-position probe examined 18 legal alternatives. No new campaigns or bot/rule edits performed.
Findings: candidate median53 versus55.5, target86/144 versus87/144. Supply exposure3.22% versus3.17%; MP4.63% versus4.11%, exploratory paired intervals include no difference. Carriers75/206 active,73 used; Bays368/620 active; Platforms109/272; Flagships2/10. MP resource-value forecast omits upkeep (actual engine settlement is correct); completion schedule already subtracts it separately, so avoid double subtraction in any fix. generated049 lasts187 with81Cycles between captures: target filtering omits a viable local assault while repeatedly killing replacement fleets (Cycle65 local assault100% AI odds,6damage,1netMP on win). Host repair/deployment remains disconnected from useful unfinished construction (matched069 CarrierCycle5→63). No voluntary-order deficit entry found. Traits12 focal appearances each per arm only, not36. No statistical trait clearance.
Recommendation only: correct forecast, local-route omission, and project host-restoration follow-through in saved situations before another versioned comparison. Do not silently launch remaining old-version blocks or pool a changed candidate into this study. Keep numerical rules unchanged pending those bounded checks. User has requested inspection, not yet this next implementation/batch. All evidence local; no publication or timers. Root historical rules, normalized current-draft text and suspended Dessica hashes verified unchanged.


## 28 September 2026 — whole-roster inspection completed

Report: whole-roster-candidate-20260927/Whole_Roster_Balance_Inspection_2026-09-28.md. All inspection processes finished. No new batch, rules, timer, publication or source/Dessica edits. Six protected root hashes,116working/frozen copies and3harness files verified in inspection-preservation.json.

Evidence:384records=240NEWgames+144exactREUSEDcontrols; primary144pairs and fresh48pairs kept separate.167,986new validated orders/270,482includingcontrols. Full384trace scan,6,523projecthistories,1,676deficitentries,21,375Cycles. Independently replayed28savedgames/14pairs,25,158orders,1,073constructionpositions,1,527routepositions,all12traits. Eight synthetic construction niches are diagnostics, not fresh campaigns. Prior422regressions+6edges are qualification,not rerun here.

Verdict: core retained provisionally; NOT a full-roster balance pass. Primary wins/36: Endurance22,Salvagers19,Fortification17,Martial16,Siege14,Void11,Dread10,Efficient8,War8,Mobile8,Swift6,Industrial5. Spread17 vs prior19. Fresh wins/12: Endurance5,Salvagers6,Fortification7,Martial4,Siege2,Void3,Dread1,Efficient5,War4,Mobile3,Swift3,Industrial5. Do not pool confirmation with primary or infer human win rates.

Primary median53,mean54.83,86/144within50–100,two>100,max138;freshmedian53,28/48within,one>100,max103;zero censored. Allthreeattackroutesused. No voluntary deficit entries. Primary S/MP exposure4.89%/3.97%,fresh4.68%/3.94%;extra pressure mainly enemy attacks,not blanket construction overspend. AllCycleordering construction→Logistics→oneevent verified. Longtails fighting,not idledeadlocks.

Keep Swift reducedupkeep (878each grossprimaryresourcesavoided),Mobile refit(76/96defencerestored),Siegevictoryreturn(primary6→14wins). Wing/Transit activations7→64/3→32;actualrolesobserved. SystemRepair spending/activationsbothdown,not solved. Elevenzero-purchaseprofiles remainunqualified. Industrial11→5primarybut5→5fresh;pairedlossesmixearlymilitarydefeat,interruption,longwar;notblanketoverspend.

Specificnextrecommendation NOTIMPLEMENTED: construction completion-reservegate can reject aSupply-only protective construction merely because existingMPbelowreserve. Local60S/4MPposition rejects finalMilitia/Shieldstage despite legalusefulprotection. SavedcandidateMilitia/Shield99legaloptions each,53reserve-rejected;Transport169/75. Notallrejectionswrong. Compareincrementalcost/remainingcommitments/protectionagainstdoingnothing,retaintrueSupplybuffer/futurecost/host/threatchecks. Qualify savedpositions andcounterexamples beforeanotherbatch. Then reviewservice/unusedniches/equalbudgetsandwholetraitroster;noforcedpurchasequota,genericbotrewrite,automaticleadernerf or arbitraryextraIndustrialdiscount. Awaituserdirection onrecommendations.



## 28 September 2026 — combined buffs/nerfs prepared; new batch deferred

User approved balancing with both buffs and nerfs and authorized preparation, but explicitly said stop just short of starting the new batch; they will start it tomorrow. Read parity-package-20260928/Parity_Package_Ready_2026-09-28.md. No campaigns/pilots/timer/publication launched. All preparation/qualification processes finished. Await explicit start request.

Candidate retains latest Swift/Mobile/Siege buffs and construction package. Endurance recovery2→1 per livingfleet/Cycle, retainszeroMPupkeep. Salvagers capturereward2→1Supply, retains2battleSupply andWingstacking. Botconstructionforecast allows inheritedMPreserveshortfall only when proposaldoesnotworsenit; retainsSupplyreserve,personnelrestorationcosts,operatingforecastpositive,deficit/host/survival/valuechecks. Enduranceforecastsupdated. Noothernumericalchanges.

Qualification:439regressions+6edgespass; sixhistoricalgamesreplayed6,288orders,28savedconstructiondecisionsreassessedbotharms.32optionassessmentsnewlyfundable,onenewlypositive,ZEROchangedfinalchoices. Do notclaimbotadoptionfixed. Eightlocalniches/arm: finalMilitia/Shieldpositive,newstartsrejectsurvival. Earlier46ground/8Mobile/15constructionprobesbotharms.36maintenance+18assault equalbudgetprobes/arm. Nofullcampaignpilots. Candidateoldhashfixture and3Enduranceexpectationsupdated intentionally; logs retained.

Preparedstudy384records/192pairs:144primarycontrolsexactreusedoldwhole-rostercandidate+144newcandidate;48freshpairs(newseeds28970000+i,map28971000+i).240NEWgamestodo. Manifeststatusprepared,completed144historicalcontrols,new_games_completed0,new_games_planned240,awaiting_user_starttrue. Noresults.json/nocandidateresults/norunning.lock. Frozencontrolidenticaloldcandidate;116working/frozencopies+3harnessesverified. UserETAwhenlaunched2–3hoursplus30–45mininspection,notstartedtonight.

Onexplicitstart:verifypreparedmanifest/inputs/norunningprocess;launchstudy.py --start hiddenwithlocalprogress/errors. DoNOT rerunprepare/duplicatecontrols. Two workers,200Cycles,replayvalidationandcheckpoints. No reminder. Afterall384complete,runstagedsummary/inspectiontools;all12traits,constructions,shortages,50–100Cyclelengthandroutes. Separateprimary36appearancesfromfresh12;nohumanSoulstormwininference. Noautofurtherbatch. Aimreasonableparity,notexactequalcounts. Ifacceptable reconcileapprovedsource/briefingsbeforeplay;otherwiseidentifyconcretecause.

Sixprotectedroothashesmatchinspection-preservation;rootrules/draft/simulatorandDessicaCycle21revision65dc4a60d17bunchanged. Noexternalpublication.



## 28 September 2026 — parity comparison started

User authorized launch. Prepared two-worker comparison started11:04:49Sydney;240newgames,144reusedcontrols. No timer. Frozen evidence preserved. Results pending.


## 28 September 2026 — parity package full inspection

Report: parity-package-20260928/Parity_Balance_Inspection_2026-09-28.md. No new campaign batch, numerical changes, timer or publication. Root rules/simulator and suspended Dessica unchanged. Full inspection:384records (240NEW+144exact reused controls),264020orders,6426projects,1673deficits,20786Cycle boundaries. Independent28savedgame replays:22529orders,908constructionpositions,1356route/factionpositions,all12traits. Digest checks passed. Evidence retained locally.

Verdict: NOT a whole-roster balance pass. Primary wins/36 Endurance26,Salvagers13,Fortification16,Martial16,Siege10,Void14,Dread9,Efficient9,War9,Mobile6,Swift6,Industrial10. Spread17→20. Current fresh wins/12 Endurance8,Salvagers2,Fortification5,Martial5,Siege7,Void2,Dread1,Efficient7,War4,Mobile3,Swift3,Industrial1. Keep cohorts separate; previous fresh seeds differ. Endurance robust across seats/maps; applied recovery nerf actual1572→1347; retains2702nominal waivedMP primary. Recommendation ONLY, NOT IMPLEMENTED: retain1heal/fullSupplyupkeep, charge ceil(ordinaryfleetcount/2)MP atLogistics. Hypothetical1520MPprimary/475fresh is snapshot cost,not longitudinal validation. KeepSalvagerscapture1/battle2 and previousbuffs;noautomaticfurthertraitchanges.

Primarymean54.87median53,92/144within50–100;freshmean50.69median49,23/48within;zero censors. Routesallused. PrimaryS/MPdeficitexposure4.48/3.72%;fresh5.06/4.72%;zero voluntary entries. Longer paired cases continued warfare; shortages chiefly enemy actions,not blanket overspend. Constructions primary2470starts989active;fresh725/303;reservefixnotgeneraladoptioncure. Eightprofilesunbought;Transport3starts0complete. Militia/Shield71legalassessments each,18feasible,0positive;Transport143legal/80feasible/1positive,beatenbyhigher-valueCannons. Recommendtargetedremainingcost/leadtime/payoff comparisons,not genericbotrewriteorforcedpurchases. CorrectedanalysisWingeligibilityusespostattackactiveprojects:primarynominal2304→2928,fresh1029→765;grossnotnetprofit. HumanSoulstormdifficultynotvalidated.

Next: discuss recommendations; no new batch automatically. If approved, local Endurance upkeep and specific construction equal-budget/saved-situation checks before bounded comparison. Reconcile source/briefings only for accepted release. Full report contains caveats and evidence paths.



## 28 September 2026 — upkeep qualification; launch deferred

User: get everything ready but stop just short of starting new batch; tomorrow. Workdir upkeep-candidate-20260928; read Upkeep_Package_Ready_2026-09-28.md. NO campaign batch/pilot/timer/publication started. Await explicit start. Manifest prepared with144verified REUSED controls,zero new games;no running.lock or candidate results. Do not confuse historical completed count with progress.

Candidate only numerical change: Endurance ordinary-fleet MP upkeep ceil(living ordinary fleets/2), retainsfullSupplyupkeep and1strength/Cyclerecovery. Mobile/deadfleets excluded;normalLogistics/locks/caps. Othertraits/constructions/botcode unchanged. Salvagerscapture1 remainsbotharms. No speculativeconstructionbuff: local comparisons corroboratevalue/deliveryproblemsbutdo notqualifyanexactnewprice/effect. Militia25S/5actions saved2MPthen destroyed in20strengthassault;Cannons9S/3actions reducedsameholdingdamageplusfleetstrength. Transportnichedependscommitment/victories;stationsscaleeffectbut5stageleadtime losesdemand. Fullreportcontainslimits.

449regressions+6edges passed,10newfocusedtests. Replayed4historicalgames/2570orders,66preLogisticsstatescheckedbotharms;181nominalnewMPcharges,noextraone-openingdeficittransitions (NOT longitudinalproof).28savedconstructiondecisions unchanged;46ground/8Mobile/15constructionprobesperarm;36maintenance+18assault+8niches perarm.170constructioncomparisons (36cost/80defence includingillegalrefusals/36transport/18station). Earlierlocalinvocation/fixture/extractionissuesretained;finalpassed.

Prepared144primarypairs+48freshpairs=240NEWgames/384totalwithreused144paritycandidatecontrols. Freshseeds28980000+i,map28981000+i. Two workers,200Cyclehorizon,validatedcheckpointing. Expected2–3hoursafterlaunch+30–45mininspection. Verifyfrozen/harness/absenceofprocess;thenonlyonexplicitrequestrunstudy.py --start hidden. NO reminders. All12traits/cohortsseparate,resources/routes/constructions/length. StagedanalysisupdatedforchargedEnduranceupkeepandSalvagers1botharms. Noautofurtherbatch. Root6hashes/DessicaCycle21revision65dc4a60d17bunchanged;116working/frozencopies+3harnessverified.



## 28 September 2026 — upkeep full balance inspection complete

Report upkeep-candidate-20260928/Upkeep_Balance_Inspection_2026-09-28.md. No new batch, rule edits, timer or publication. Full384records (240NEW+144reused),270050orders,6684constructionhistories,1696deficits,21227Cycleboundaries. Independent28savedgame replays22445orders,897constructionpositions,1357route/factionpositions,all12traits. All digests matched. Protectedroot/frozenhashes unchanged;DessicaCycle21revision65dc4a60d17b preserved. Inspection processes finished.

Verdict: retainEndurancehalfMPupkeep/1heal candidate; clearimprovement but NOTunconditionalall-content signoff. PrimaryEndurance26→12,fresh7→3. Primaryspread20→12;11traitswithin7–17;Fortification19outsidepreferredband. Candidateprimary wins:Endurance12,Fort19,Martial17,Salvagers16,Void14,Siege11,Efficient10,War10,Dread10,Industrial10,Swift8,Mobile7. Fresh:3,7,8,7,4,3,3,4,1,2,3,3 respectively. All144pairswithoutEnduranceexactlyidentical;cohortsseparate.

Importantcost:EnduranceprimaryS/MPdeficitexposure11.49/7.34%,fresh15.53/7.68%;mostlyenemyattacks,noEnduranceMPentrydirectlyLogistics. MoreMuster/Ration,lessReinforce;notgenericbotbugorconstructionoverspend. Overallprimary4.77/3.99%,fresh5.28/4.22%;zerovoluntaryentries. Median53bothcohorts,91/144and30/48within50–100;zerocensors. Routesallused. Longpairedcaseskeptcapturing. Logged1471/450candidateEnduranceMPupkeepisassessedcharge,notnecessarilyrealizeddeductionunderlocks/netsettlement.

RecommendationONLY:notimplemented.FortificationDefendSupply+3→+2,retainfreeDefend,+2extrahealingandDefended;qualifysavedstatesbeforefurthercomparison. Primary1357Defends4044Supply,466zerorepair;zeroReinforce. No immediateMartial/Salvagersnerf. Constructionsunchanged,8profilesunbought;primary1015/2528active,fresh347/874;stationslowcompletion. OnefreshIndustrialTransportcase171completed2S,returned9extraMP;samebotharms,notEnduranceimprovementorfullpricevalidation. Targetconstructioncost/deliverylocalcomparisons,notgenericbotrewriteorforcedpurchases. CandidateMilitia/Shield66legal,13feasible,0positive;Transport166legal,73feasible,0positive in selectedpositions (notincludingrarecompletedexample). Noautomaticnewbatch. Source/briefingconsolidationneededforacceptedrelease;humanSoulstormdifficultynotvalidated.


## Fortification/construction local qualification — 28 September 2026

Directory fortification-construction-review-20260928. Completed local checks only; no new campaign/runner/timer/publication. Fortification candidate now grants +2 Supply on Defend, retains free costs/tier+2 repair/Defended; narrow bot correction chooses Reinforce for healthy unthreatened holdings in its Supply branch. Endurance retained. 459 tests+6edges pass; 4,481 saved orders replayed across four games; 111 construction snapshots; 71 Fortification faction snapshots (case022 replayed again). 9/71 decisions change Defend→Reinforce; all legal. Control188files and protectedroot6files unchanged.

Price sensitivities for five Majors at5/4/3/2 Supply perstage plus Transport2 in discounted variants changed0/2/2/3 choices outof111. All-host checks and 288synthetic situations pervariant show a blanket discount is not a qualified solution. Runtime discounts are NOT adopted engine rules. Report Fortification_Construction_Qualification_2026-09-28.md records exact tables, limits and next focused niches: Militia avoiding isolation; VoidShield off-threshold/repeated attacks; PlanetaryShield maintainedvoidcontrol. No automatic long batch. Fortification mechanically qualified, campaignwinrate not yet assessed. Preserve original frozen studies/Dessica.

Supplementary local niche matrix completed:360setups/356legal attacks (four strength5Cannon attacks unavailable after precommitment fire). Militia prevented isolation in12matched cases; VoidShield works off damage thresholds and atpositiveIntegrity; full PlanetaryShield blocksdamage withmaintainedvoidcontrol, damagedoneinactive. These supersede the pending-niche line above. No new rules/batch. Militia general economic value remains unresolved; shields have verified distinct niches and are not universally dominated by Cannons.

## Militia local qualification completed — 29 September 2026

Work directory militia-qualification-20260928; report Militia_Qualification_2026-09-29.md. No running batch/timer/publication. Proposed candidate adds completed positive-Integrity Militia waiver of host Defend Manpower cost, retaining normal Supply/action/repair amount and all existing defensive commitment/isolation effects. Applies eligible planets/stations/MobileCapital; no extra Fortification benefit; no income/rationing/Integrity repair. Keep existing5Supply/stage5Integrity price. Discount variants diagnosticonly, NOT engine rules. Root/Dessica unchanged;control189files exact; frozen inputs verified.

473regressions+6edges pass. Four alternatives across192controlled6Cycle siege setups (768trajectories, notcampaigns); candidate saves personnel under moderate assault, remains Supply-limited, loses benefit on destruction. Held38/48Militia setups in everyvariant; lowMPstrength15 capture delayed1–2Cycles, notprevented. Same111historical construction positions (4,481previouslyreplayedorders),170/171legalMilitia assessments pervariant;zero positive saved estimates andzero changed choices.48synthetic valuations pervariant:positive1current/3cheaper/2local/3both. Do NOT claim uptake or winrate fixed. Candidate narrow bot estimateone survivingDefend, quarterweightremote, noFortstack. Report recommendslocalwaiverwithoutpricecut asprovisionalpackage; nextboundedwholepackagecomparisonneeds targetedMilitia evidence alongside campaign results. No broadbotrewrite or forcedbuy. Await next batch instruction; nothing launched.

## Combined package batch launched — 29 September 2026, 10:08 Sydney

User explicitly authorised begin. Directory combined-package-study-20260929; runner PID16128 (runner.pid), two workers, no timer/reminder/publication. 384records/192pairs:144verified reused controls plus240NEW games (144matched candidates+48fresh pairs). Primary36trait appearances perarm; fresh12. New fresh seeds/maps29980000/29981000 plus0..47. Controls are upkeep-candidate-20260928/candidate; new candidate is militia-qualification-20260928/candidate. Both retain testedEndurance; candidate changesFortification+2/healthyresupply andMilitia localDefendMPwaiver atunchangedprice withbounded valuation. Frozeninputs validated,473regressions+6edges on exactqualifiedsource. Initialmanifest running, noerrors. Estimate2–3hours; check around12:30Sydney, allowto13:10foroutliers.

Read manifest.json, study-progress.txt and study-errors.txt; inspectPID/lockbeforeanyresume. Do notduplicate. Newgames independently replayvalidated; incomplete/failedcases retained. Oncompletion perform fullinspection beyondsummarise.py: all12traits separatelyprimary/fresh, pairedoutliers, campaign50–100Cycle target, deficitsandcauses, combat routes, construction completion/use, Fortification/Endurance andMilitia mechanisms. NoMilitia purchases inlocal111snapshotcheck: do NOT claimuptakefix without evidence; targetedcontrolledsieges remainseparateevidence, notcampaigns. SourcebaselineandDessica preserved. Noautomaticnextbatch. SeeStudy_Plan.md forscope.


## Combined package full inspection completed — 29 September 2026

Report: combined-package-study-20260929/Combined_Balance_Inspection_2026-09-29.md. All384records/192pairs complete;240newgames172900validatedorders,274555totalorders. Full history inspection6766projects1726deficits;20-game decision replay20299orders864constructionpositions1212route/factionpositions, all12traits. Player640setups288series2examples pass. Protected root hashes unchanged. No running batch/new timer/publication/rule edits.

Retain Fortification correction: primary19→12 wins/36,fresh7→5/12. Martial19/36 still exceeds7–17 tolerance;Efficient9/12fresh unchangedcontrol, policy exposures differfresh. Candidate mean56.51median54.5;125/192within50–100,63shorter,4longer. Deficits859vs867, zero own-voluntary-order triggers. All three routes used. Construction3360starts1344everactive;34.9%spending neveractive, nearcontrol. Militia0purchases;93legalcandidate savedoptions0positive, remains provisional with separatecontrolledsiege evidence only.

Specific case187blocked-target movement stall35Cycles:29strength vs30,95S92MP atCycle65; repeatedreplanning resetsblockedobjective. Saved replay1169orders and capacity projections recorded; projections omit enemyresponse, do not prove safeattack. Recommend narrow alternate-objective/repair planning correction and savedcounterexamples, then constructioncompletion/valuation inspection(SystemDefence,Repair,SiegePlatform,Carrier,StormTransit,Militia repeatedDefend). Noautomaticlarge batch or blanketcostchanges. Source/Dessica unchanged. Await user's next instruction.


## Planning correction and construction diagnosis — 29 September 2026

Staged planning-review-20260929/candidate; only existing operational_bots.py changed. Frozen study/root rules and Dessica preserved. Stale remote blocked targets can choose an alternative passing unchanged assembly safety checks; reselecting same target no longer resets progress. 473existing+5focused tests pass. Focused case187 uses aged savedCycle65state, not campaign continuation; no new campaign outcome claims. First regression call from wrong cwd had12missingfixture errors, corrected cwd passes unchangedtests.

Construction review: 34positive feasible legal unfinished-option comparisons while new start selected across22game/Cycle combinations;12higherrawfinishvalue need emergency-context interpretation. More importantly newstart forecast assumesqueuedcompletion but actionmaystartnewinstead; economicpayoutdate omits queuedelay evenwhenfundingchecksqueue. Recommend ordered finish-vs-new plan comparison plus unifiedactivationdate, preserve emergencies. Militia93legaloptions0positive,56unfunded;10eligiblecostedlocalDefend casesonly3nonzerosavings. Recommend bounded repeatedassault/survival/Defend valuation, noflatmultiplier/freeSupply/Fortstack. No constructionrulesorvaluationeditedyet, no newbatch/timer/publication. Report Planning_and_Construction_Review_2026-09-29.md; logs and saved comparisons local.

Emergency-context replay completed: five saved games,6033orders verified. All12higherrawfinishvalue comparisons coincide with defensive-emergency filtering; do NOT call them ordinary score-ranking bugs. Check emergency project activation horizon separately. Queue/action and payout-date recommendations remain. All local work complete; no batch running.


## Construction forecast corrections completed — 29 September 2026

Directory construction-forecast-review-20260929/candidate; report Construction_Forecast_Corrections_2026-09-29.md. Retains blocked-target correction. Adds bounded two-project ordering, unified scheduled economic payouts, emergency protection activation deadline and finite repeated-Defend Militia valuation. Bot-only: no gameplay rules/prices/trait effects changed. 486tests pass;3savedgames4363orders replayed,31snapshots evaluated botharms62legal submissions.8choiceschange:3starts→existingBuild(1/2/2Cyclesremaining),5late emergency starts→none;23unchanged. Militia43legaloptions0positive inboth; no uptake claim. Initial failedprototype/emergency and obsoleteone-Defenddiagnostic updates documented inreport. Rootprotectedhashesmatch; no newcampaign/timer/publication. Ready for user-authorised bounded comparison; NOT already running. Limitations:two-project heuristic, conservativeemergencydeadline, fixedvisiblebattleprobability and conservativepaidbaselineMP forMilitia.


## Construction forecast paired batch launched — 29 September 2026, approximately19:37 Sydney

User authorised carry on. Directory construction-forecast-study-20260929; runner PID16876, two workers.192new candidate games against192exact verified reused controls fromcombined-package-study-20260929/candidate (384records192pairs). All12traits, same full schedule/seeds/policies/maps;144primary36appearances/trait and48confirmation12. Confirmation is reused, NOT fresh independent holdout. Candidateconstruction-forecast-review-20260929 includes movement+construction botcorrections; rules unchanged.486tests plus31savedpositions passed beforelaunch; frozeninputs/reusechecks/rootprotectedhashes verified. No timer or publication. ETA2–3hours, allowup to4; checkaround22:00Sydney withwindow21:40–22:40.

Readmanifest,progress,errorsandPIDbeforeanyresume; neverduplicate. Oncompletion fullpaired inspection: traitcohorts separately, pacing/deficits, constructioncompletion/neveractivespend, emergencyinactivity, blockedtargetstalls, Militiavaluation/uptake. No automaticnextbatch. Priorreport documents conservativeemergencywindow andMilitiaassumptions. Userwantedunder4hours; updateETAfrommeasuredprogress ifasked.


## Construction forecast full balance inspection complete — 29 September 2026

Report construction-forecast-study-20260929/Construction_Forecast_Balance_Inspection_2026-09-29.md.384records192pairs complete,192newgames138941validatedorders,277643total. Allfrozen/reused192control/protectedroot hasheschecked. Noerrors/censors. No newbatch/timer/publication/ruleedits.

Candidate waste11111→8922Supply(-19.7%);starts3360→3060;everactive1344→1342;totalspend31858→29191. Mean56.51→56.88Cycles;within50–100125→129/192;over1004→2. Deficits859→877;S exposure4.67→4.90%,MP4.08→4.50%;zero voluntaryselfdeficits. Evententries96→119,hostileorder750→740. All three routes remain used. Maxcapturegap36→21;case18735→3. Primarywins: Dread10,Eff15,End13,Fort13,Industrial13,Martial16,Mobile12,Salv17,Siege11,Swift6,Void10,War8. Swiftbelow7–17toleranceandcombined14→8wins;equal2386alivecyclesbutlowernetincomeandspending,moredeficits. Secondary reusedconfirmation NOTfreshholdout.

SystemDefence46starts0active;SystemRepair104/11;Militia0. Targetedreplay3games2697orders100constructionpositions156route/factionpositions.32stationBuild assessments:30feasiblenonpositive,2deficit;only4emergency,0positive. Do NOT blameemergencyfilter forsampledabandonment. Case44RepairStationstartsCycle3positivebasedondamagedfleets;ExpandFleetCycles8/9 anddepartureCycle11 remove demand. Recommend stationforecastincludeaffordablemanualrepair/departure andenemyclearance atactivation;checkdurablefront/returningfleet contexts beforepricingchanges. Keepqueue/payout/stallfixes;retainemergencysafeguardprovisionally. InspectSwift earlyexpansion/incomelosses beforetraitbuff. Militia remainsprovisional. Noautomaticnextbatch. Allworkcomplete, nothingrunning.


## 30 September 2026 — next-priority construction diagnostic pass

Completed local checks under the accepted station-only baseline: 72,000 enumerated dice positions across 180 conditions (69,600 legal assault resolutions; 2,400 blocked), 68 construction cost checks, 80 fixed-outcome probes, 36 transport calculations, 18 immediate service checks and 18 repair-demand comparisons. These are controlled positions, not new campaign games. Report: `construction-priorities-review-20260930/Targeted_Construction_Findings_2026-09-30.txt`.

Shield effectiveness changes with fleet strength thresholds; Cannons do not universally dominate. Militia preserves personnel but does not solve overwhelming attacks. Stations can provide real recurring fleet service, but ordinary batched expansion is a materially cheaper comparator than repairing every single point immediately. Price/delivery concerns remain. Proposed (not adopted): 15 Supply/five actions for Militia, Void Shield and system stations, and 6/three for ordinary Transport; retain Planetary Shield immunity/effect and current prices for now. Industrial interactions explicitly require checks: the proposed Major price becomes 4 total under current Industrial rules. No extra effect buffs or trait numbers adopted.

Remaining work: repeated-pressure/build-interruption comparisons, saved station decisions at proposed costs, and fleet-support/naval alternatives. Broader unused catalogue is not signed off. Existing larger trait sample is reference; Swift late resilience remains unresolved. No campaign batch, timer or publication started. Accepted frozen inputs verified unchanged.


## 30 September 2026 — targeted construction follow-up

Completed 144 bounded lifecycle comparisons, 2,400 naval dice resolutions, six Repair Tender probes, plus 2,697 validated historical orders extracting 127 station positions and 254 paired price-decision assessments. See `construction-priorities-review-20260930/Construction_Followup_Findings_2026-09-30.txt` for limits and findings.

Keep Militia/Void Shield 15-Supply candidates provisional: they resolve a funded one-point interruption but cannot complete under every-other-turn assault. Industrial cost falls 12 to 4 and must be monitored. WITHDRAW the proposed blanket station discount from the next package for now: positive Build continuations stay 3; seven choice changes all Industrial. Known abandoned station remains negative. Escort has a demonstrated tactical niche; no automatic buff. Recommend a separate local candidate removing Repair Tender's preceding-combat exclusion while retaining positive Integrity/activity and Phase-0 timing; not implemented yet. Transport 6-Supply proposal remains provisional, without a new lifecycle comparison this pass.

No accepted changes, full campaign batch, timer or publication. All registry-pinned baseline files verified unchanged. Remaining: Tender candidate checks, Transport lifecycle/equal-window economics, and unreviewed construction niches; broad catalogue/trait balance not signed off.


## 30 September 2026 — construction value candidate implemented

User authorised proceeding with the shortlisted recommendations. Isolated implementation: `construction-value-candidate-20260930/candidate`. Militia/Void Shield 3 Supply per stage; Transport 2 per stage; Tender repairs at Phase 0 after combat if surviving/active. Station prices, Escort, Planetary Shield and traits unchanged. Bot automatic-repair forecast aligned, and cheap-profile affordability gate corrected without allowing voluntary deficits. The candidate-local frozen-rule manifest was repinned; accepted registry independently remains unchanged.

495 regressions and five targeted tests pass. 72 fixed twelve-Cycle benefit schedules show ordinary Transport costs 6 Supply and returns 10 extra MP at five victories with >=3 commitment, versus Training 9 Supply/9 MP; sparse/small assaults favour Training. These are conditional marginal returns, not campaign outcomes. Industrial Major discount and combat-Tender sustain remain aggregate balance questions.

Read `construction-value-candidate-20260930/Candidate_Readiness_2026-09-30.txt` for exact scope, caveats and next gate. Ready as an isolated candidate for a bounded paired campaign comparison; no campaign batch/timer/publication started, accepted station-only baseline remains. Full catalogue and Swift not signed off.


## 30 September 2026 — construction value comparison running

User approved proceeding. Launched `construction-value-candidate-20260930/study.py --start`, PID 8624, two local workers. 48 new candidate games against 48 exact-input/schedule reused station-only controls; twelve appearances per trait, reused secondary schedule (not fresh holdout). Case 0 smoke passed: 51 Cycles and 621 replay-validated orders, counted among the 48. Do not launch a duplicate. Manifest/progress/error logs and PID are in that directory. Estimated 45–60 minutes for run, 10–20 minutes subsequent inspection; no timer or heartbeat.

On completion require 96 rows (48 new/48 historical), matching initial hashes, all replay validation, no failures; run inspect_full.py and inspect Tender outcomes/Industrial interactions before recommending promotion. Saved plan Study_Plan.txt. Accepted baseline unchanged; no publication.


## 30 September 2026 — construction value batch fully inspected

Read `construction-value-candidate-20260930/Construction_Value_Balance_Inspection_2026-09-30.txt`. 96 records/69,273 validated orders (48 new/34,677 new orders), all complete, no failures. 46/48 finals identical; all winners unchanged. Mean56.10->56.25, target32->33/48, deficits239->242; zero voluntary deficits. Starts733 both, active343->345, never-active spend2057->2055.

CRITICAL coverage failure: no Militia/Shield purchases; Transport1start/0active, Tender3/0. Revised effects never operate. Do not promote or run another unchanged random batch. Five-game decision replay4,473 orders/115positions found118 legal starts each for Militia/Shield, none positive. Transport had a legal positive final Build at case43 Cycle78 but emergency protective filter excluded it; thereafter host damage blocks. Tender mostly nonpositive, not generally emergency blocked. Case7 extra3deficits/7Cycles result after planner refresh from a newly affordable but unchosen Transport option; reproduced same saved state. Case43 same actions with2Supply savings only.

Next recommendation: bounded completed-and-used operational comparisons, plus exact Transport final-stage emergency counterfactual; no broad bot rewrite or extra discounts without realised benefit evidence. Accepted station-only registry unchanged. No tests still running, no timer, no publication. Traits unchanged; larger previous sample remains reference.


## 30 September 2026 — focused operational checks complete

`focused-construction-review-20260930/Focused_Operational_Findings_2026-09-30.txt`: corrected the suspected Transport-filter diagnosis. Exact case43 fixed-order counterfactual completes the project for2Supply but delivers0 extraMP: its last assault precedes completion, then rationing prevents further assaults. Both1,313-order branches legal toCycle89; recorded final hash matches. KEEP emergency filter; raw opportunity valuation was optimistic here, not a proven bad final choice.

368 operational windows plus368 reserve-sensitivity windows and54 actual assault missions demonstrate conditional roles. Militia trades24 moreSupply for15MP preserved in one prepared-defence fixture; Tender trades9 extraSupply/7Construction actions for4MP/4Fleet actions versus ordinary repairs; Transport gives10 extraMP after5 three-MP victorious assaults versusTraining9, but only6 versus9 at3 assaults. Shield still costly under heavy pressure; no further effect/price buff supported. Initial resource-capped mission pilot preserved/excluded; v2 uses40Supply/30MP.

No bot edits, new long batch, timer, publication or baseline promotion. Candidate prices/mechanics preserved. All accepted and frozen study hashes unchanged. Natural construction uptake and wider trait uncertainty remain; no claim of complete balance. Next limited opportunity-forecast review should use public state, not recorded future knowledge.


## 30 September 2026 — narrow bot opportunity audit

Completed the approved Transport, construction timing and defensive/Tender estimate inspection. Isolated candidate: `opportunity-audit-20260930/candidate`; report: `opportunity-audit-20260930/Opportunity_Audit_Findings_2026-09-30.txt`. Added a public-state affordability bound to Transport forecasts; no rule changes or forced purchases. Exact case 43 replay verified 1,313 orders. The saved positive Cycle 78 estimate remains positive because current income supports later assaults; actual later enemy action prevents them. Keep the emergency filter; do not call this a resolved uptake problem. Construction timing already correct; controlled results do not justify general defensive/Tender estimate inflation. 503 regressions and two saved-state integration checks. All 29 accepted baseline hashes unchanged. No general campaign batch, timer, publication or accepted promotion. Next work should address the remaining construction value decision, not assume a further broad bot rewrite is necessary.


## 30 September 2026 — defensive construction cost recommendation

Completed local assessment in `defensive-cost-review-20260930/Defensive_Cost_Recommendation_2026-09-30.txt`. Recommend retaining Militia at3Supply/stage (15base total), proposing VoidShield2Supply/stage (10base total), keeping five stages and1Supply/Integrity repair. Industrial remains4total because of its floor/stage discount. Isolated combined candidate in `defensive-cost-review-20260930/shield-price` includes prior Transport/Tender proposal and Transport opportunity correction; NOT accepted/promoted. Ran184 short controlled windows,36Shield comparisons and148 exact unchanged controls. Lower Shield price saves prepared-case Supply but changes no retention outcomes and does not fix interrupted construction; mixed Manpower outcomes explicitly recorded. No campaign batch/timer/publication. Await package approval before any long campaign comparison.


## 30 September 2026 — combined construction comparison launched

User approved continuing. Study `combined-construction-study-20260930`:48 new candidate games plus48 exact verified saved station-only controls; two workers, all12traits equally represented,200-Cycle safety ceiling, replay verification. Candidate combines Militia15Supply, Shield10Supply (five stages), Transport6Supply, post-combat Tender repair and Transport affordability bound; emergency filter retained. No accepted baseline promotion. Same reused secondary schedule, not fresh holdout. Previous run33minutes; estimated45–60minutes running plus15–25minutes inspection. No timer/publication. On return read manifest and progress, preserve failures, do not duplicate runner; after completion inspect construction benefit/activation/maintenance, shortages, routes, duration and traits, including changed pairs.


## 30 September 2026 — combined construction full inspection complete

Report: `combined-construction-study-20260930/Combined_Construction_Balance_Inspection_2026-09-30.txt`. Inspected all96 traces/69,273orders; additional exact4,473-order replay across five cases with106decision positions. Mean56.104->56.25Cycles; target32->33/48; deficits239->242 but exposure marginally lower; no own-action deficits. All winners/trait totals unchanged.46/48finals identical to station-only;47/48 identical to previous candidate. No Militia/Shield built, no Tender active, no Transport starts. Sampled119legal Shield options,96funded,0positive; Militia118/94/0. Transport fix avoids unfinished Transport but substitutes3Supply BombardmentBay destroyed before activation; saves1Supply versus previous candidate, no outcome improvement. Case7 has all extra deficits after enemy ground assaults with no recent construction spending; same as prior candidate. No material aggregate regression, but revised construction utility unvalidated in natural campaign play. Keep package provisional and station-only accepted; no repeat identical batch, no general bot rewrite or trait-number change justified. Prior controlled operational evidence supplies conditional effects only. If further pre-play work requested, use narrow equal-resource saved threatened positions including failed replacement investment; no new run started. Frozen/baseline hashes intact.


## 30 September 2026 — saved investment choices resolved

`saved-investment-review-20260930/Investment_Choice_Findings_2026-09-30.txt`: five same-resource fixed-order continuations,3,994 validated orders, no illegal continuation; recorded branches exactly reproduced. Case10Cycle33 Tender completion versus chosen Bay build versusNone: active Tender provides no strength restoration through end37; saving3Supply is absorbed at next Logistics ceiling. Case43Cycle77 saving versus failed Bay start:3Supply saved only until next Logistics ceiling, identical MP/fleet histories and elimination89. No repair choices legal at either intervention. No evidence for forced completion, broad investment prohibition or another effect buff. Retain provisional package, stop identical batch repetition; next decision is creator adoption for monitored playtesting, not a claim of complete trait/catalogue balance. No code/rules changed; accepted baseline untouched.


## 30 September 2026 — fresh trait spread test started

User requires max25percentage-point highest-lowest trait win-rate spread BEFORE playtest; previous suggestion to playtest now is superseded. Authorised buffs and nerfs, Dread largest buff. Larger36-appearance reference disagrees with blanket nerfs of latest50%traits: Mobile12,Siege11,Fortification13 versus Efficient15; Swift6,Dread10. Previous versions are contextual only, not pooled. Candidate `trait-spread-study-20260930`: Dread surcharge2/asset (was1); Swift fleet creation1Supply/0MP (was1/1); Efficient Reinforce/Muster5(was6), bot yield estimates updated. Other9traits unchanged; Martial/Salvagers watchlist. BOTH arms retain identical provisional combined constructions to isolate traits. Accepted station-only baseline untouched.507regressions pass; first actual candidate game replay-validated. Fresh144paired scenarios/288games,36trait appearances per arm,two workers,200Cycle horizon; no old controls reused. New seed range30960000–30960143, checked against11saved schedules; scenario allocation balanced and locked. Max spread9wins/36 qualifies raw25pp threshold; inspect uncertainty and map/seat/policy consistency too. No automatic promotion or tuning against validation outcomes. ETA3–4hours plus20–30mininspection; no timer/publication. On return read manifest/progress/PID, do not duplicate. After complete run inspect_full.py and rank traits per arm with max-min, duration/shortages/routes, new trait usage, subgroup and paired changes.


## 3 October 2026 — Six-stage trait inspection completed
288 games, 144 pairs, 195809 previously replay-validated orders. All trace final hashes/order counts and frozen source hashes checked; accepted baseline hashes verified unchanged. Candidate spread27.8pp vs control44.4pp: still fails25pp requirement. Dread3->10 wins; Efficient9->9; Industrial6->7; Mobile19->17 (each/36). Swift zero-Manpower creation occurred nine times during MP deficits in six campaigns. Full report: trait-spread-study-20260930/Trait_Spread_Full_Inspection_2026-10-03.txt. Recommendations pending approval: Industrial +2 progress on subsequent Build actions (retain discount/start2); Swift block deficit creation and use fixed+5 Expand instead of unlimited full-capacity restore; retain Dread2 and Efficient5 in primary candidate. No new batch, timer, rule promotion or campaign-state edits. Report also records construction-uptake limitations, route/pacing/shortage analysis and legitimate merge tradeoffs.


## 3 October 2026 — Coordinated six-trait package running
User approved the full six-trait recommendation and96-game comparison, aiming under3hours. New isolated directory: trait-package-study-20261003. Current reference is prior trait-spread-study-20260930 CANDIDATE cases0-95, copied as new control with96result/trace hashes recorded in reused-reference-provenance.json. No reference games rerun. New candidate96games provides24appearances pertrait,48maps perfamily; same paired seeds/scenario/controllers. This is a development comparison, not fresh independent confirmation. Frozen source and harness hashes in manifest; accepted29baseline hashes checked unchanged.
Changes: Mobile living capital+1Supply Logistics upkeep; Martial bonus5->4MP; Swift deficit creation blocked and Expand+5Strength; Fortification Defend+3Supply; Void Expand+4Strength; Industrial subsequent Build/Upgrade+2progress, initial2/discount retained, Repair unchanged. Bot construction timelines and restoration estimates aligned. No construction prices changed.
515 regression tests pass (8new package checks);56 finite-horizon catalogue comparison estimates recorded, with limitations in Construction_Check_Notes.txt. Saved-situation tests in regression passed. Prior failed test logs retained: initial invocation used wrong cwd for saved fixture paths, old-rule assertions updated, new multi-turn test fixtures corrected to reset spent phase and repair only completed constructions. No failures silently omitted.
Started local hidden finite runner run_batch.py at approximately09:37 local time. WrapperPID21884; coordinatorPID18108; one worker. progress.txt/errors.txt/manifest.json track status. Do not duplicate.96new games plus96retained reference rows =>192total planned; first status running96total/0new. Each new game replay-validates before saving. On completion summarise.py creates completion-summary.json, which requires full inspection before sign-off. No timer/automation created. Check back roughly2.5hours afterlaunch, target2.5-3hours including inspection; longer campaigns can overrun. Preserve failed cases and frozen inputs if a failure occurs.
Acceptance max25percentage-point spread (=6wins/24), alongside pacing/shortages/routes/exploit and construction checks. Do not promote or launch another batch automatically. Root accepted baseline and suspended Dessica untouched.


## 3 October 2026 — Coordinated package full inspection completed
Study trait-package-study-20261003:96new+96reference games,133932previously replay-validated orders; all192trace final/count checks and frozen/reference/baseline hashes verified. Runtime121.9minutes, no failures/censoring. Spread29.17->33.33pp FAILS25pp. Fortification6->13/24, Void5->11, Martial12->9, Salvagers12->9, Swift10->9, Industrial5->7, Siege8->7, Mobile10->7, Endurance8->7, WarEconomy10->6, Efficient5->6, Dread5->5. Eleven non-Fortification traits spanexactly25pp. Recommended pendingapproval: retain fivechanges and returnFortificationDefendSupply3->2; do notpromise rollbackguaranteespass. Defend givesReinforceincomeplusfreeheal/status at3;522->700Defends and1044->2072realisedSupply. Industrialactivation67->89 andmedian3->2Cycles; Swiftdeficitcreations7->0. Pacingmean55.21/median55,60/96targetrange; shortagesroughlystable. Sparseconstructionuptake andIndustrialearlyCarrierchoicesremainlimitations. Report Full_Balance_Inspection_2026-10-03.txt, detailedJSONevidenceand13pairedcasehistories saved. No newbatch, rulepromotion, publication, automation or Dessica edits.


## 3 October 2026 — Fortification confirmation batch started
User approved proceeding after full inspection. New isolated folder fortification-confirmation-20261003. Sole production change versus previous candidate: shared_sim.py Fortification Defend Supply3->2. Other five changes retained exactly. 518 regression checks passed, including3new confirmation tests. Initial failed test log preserved: a test expectation replacement accidentally changed ordinaryReinforce expectedincome; corrected test to13, no production change.
96newcandidate games, reference96from trait-package-study-20261003 candidate;24appearances/trait,12/mapfamily,8/seat. Development scenario reuse, not independentholdout. All reference copies and pins validated;29accepted baseline hashes remainunchanged. No Dessica edits.
RunnerwrapperPID4932; coordinatorPID11028. manifest.json/progress.txt/errors.txt trackprogress. One worker, replayvalidation foreachnewgame, no duplicate launch. Expected2.5-3hours fromlaunch includinginspection; previousbatch121.9minutes. No timer or automation. run_batch.py performs finite post-completion summarise.py, inspect_full.py, inspect_mechanics_detail.py and paired_outcomes.py automatically. These write evidence; they do not promote rules or supply final human-facing verdict. On nextcheck, distinguish game completion from post-run inspection completion and conduct remaining interpretation. Read Rules_and_Plan.txt and approved-change.json.
Acceptance <=25pp roster spread (<=6wins/24), plus pacing/shortages/routes/construction review. All96scenarios retained; no outcome filtering or automatic nextbatch. Prior studies and approved baseline unchanged.


## 3 October 2026 — Confirmation optimized after user challenged redundant runtime
User correctly challenged96full reruns for one isolatedFortification correction. Originalwrapper4932/coordinator11028 stopped; currentworker8976 was allowedtofinish. Ninefullcandidate games retained (including oneFortificationcase). optimized_run.py PID24280 now running oneprocessatime. Remaining23Fortificationcases fullysimulate; remaining64non-Fortificationcases first attempt guardedreplayrequalification undercandidateengine. Earlier8unaffected games were alreadyfreshlysimulated. All96scenario outcomes remain in denominator; no cherry-picking.
Reuseproof: productiondiff is exactlyFortificationDefendSupply3->2; allother siminputhashes identical. Eligible scenarios have noFortification ininitial/finalplayers or summonorders, horizon0 andoperational/trait_operational controllers only. Thesecontrollers use direct estimates/one-action trials: evaluatingSummon itself doesnotinvoke a futureFortificationDefend. Guardedreplay checks allplayers beforeeveryactualaction and validates everyrecordedpostactiondigest/finaldigest undernewengine. This revalidates recordedorders; it is not a freshbotdecision run. Anyguard/replayrejection is preserved and triggers afullsimulation instead. Copiedresult explicitlymarked unchanged_trace_replay_requalified with originalinputhashes/provenance. Fullsim and reusedcandidate counts separate inmanifest.
Frozenstudy.py/rulefiles untouched; optimizedrunner hashes recorded separately. optimized-progress.txt/optimized-errors.txt now authoritative liveoutput. No duplicatelaunch. Post-run summary/metric scripts retained. Updatedexpectedremaining runtime roughly30-45minutes, dependentonreplaychecks andaffectedgames, insteadof2.5hours. Inspection stillrequired, and25ppacceptance unchanged. No timer/automation.


## 3 October 2026 — user redirects from isolated correction to broader release work
User: narrowone-traittesting leavesotherknownproblems untouched; broaderchangesrequested. Stopped optimizedcoordinator24280, preserving its currentchild and allcompletedresults. fortification-confirmation-20261003 manifeststatus interrupted_for_broader_package; do NOTresume automatically. Remaininghistorical partialresults are notfullbalanceevidence.
Prepared release-package-review-20261003/Broader_Release_Package_Proposal_2026-10-03.txt: proposedFort2, Dreadflat2plus2perasset, Efficient6, WarEconomy6; retainfivepriorchanges; proposedMilitia10total, SystemDefence/Repair15total, Tender6total withoutIntegrity/effectchanges; fixconfirmedmilitaryconstructioncompletion-survival bypass. Proposals notimplemented/launched. Source/WebAppreleaseconsolidation should accompanyqualification ratherthan beleftuntileverybalanceiterationends. Onecombined96gamebatchafterqualification; noautomaticrestart or timer. Probe positivelyvaluedCarrier/SiegePlatform bypass completion_survival whileTender invokesit; evidence military-survival-check.json. Noacceptedbaseline/Dessica edits.

## 3 October 2026 — broader release package launched
User approved the coordinated package with “Please proceed”. New isolated directory: release-package-study-20261003. Narrow fortification-confirmation remains interrupted; do not resume or merge its partial evidence.
Implemented: Fortification Defend Supply 3→2; Dread surcharge 2 per engagement plus 2 per asset; Efficient Reinforce/Muster 5→6; War Economy Logistics bonus 5→6; Militia and Tender Build cost 2; System Defence/Repair cost 3. Other completed six-trait candidate settings retained. Military construction planning now applies completion survival exactly once, discounts benefits and retains expenses. Efficient bot forecast yields aligned, including construction_choice.
Qualification: 520 regression tests pass (515 existing expectations updated for authorized changes plus 5 new package checks); 56 construction comparisons across control/candidate; three saved Industrial Carrier positions (23,29,91) reconstructed and assessed without mutation. Their initial scores remain unchanged: this correction is NOT evidence those losses are fixed. Targeted risk tests verify reduced positive benefits, unchanged expenses, one assessment, and unsafe rejection. Initial wrong-working-directory regression attempts preserved, corrected before qualification. Accepted baseline's 29 frozen hashes checked unchanged.
Candidate guide and local HTML: Campaign_Release_Candidate.txt and campaign-release-candidate.html inside the new study. These consolidate traits/prices/timing/worked example; explicitly not a completed editorial audit of every historical source rule, not published or promoted.
Launched 13:47:40 local (+10:00), wrapper PID 27524, run_batch.py, one worker. At 13:48:06 status running, 1/96 NEW games complete, no failures; 96 exact-source reference games reused (97/192 records). Estimated 2–3 hours from launch, approximately 15:50–16:50 local. No timer, scheduler or reminders. Do not launch a duplicate. Read manifest.json, progress.txt and errors.txt for status; distinguish 96 reused controls from new games. All new games replay-validated. Reference provenance in reused-reference-provenance.json. Scenario reuse means development comparison, not independent holdout.
After completion run_batch automatically runs summarise.py, inspect_full.py, inspect_mechanics_detail.py and paired_outcomes.py. Then manually review all twelve traits against <=25pp spread, pacing, shortages, attack routes, construction delivery/costs and exploit effects. No automatic promotion or further batch. Preserve Dessica Cycle21 revision65dc4a60d17b. No GitHub changes this turn.

## 3 October 2026 — coordinated release package completed
release-package-study-20261003: all96 new games completed/replay-validated in113.6minutes, no failures or horizon censoring;69292 new orders,136163 including96 retained controls. Completed saved-trace inspection192traces/2921projects/896deficitentries. Paired analysis helper corrected to use its own directory (previous copied hardcoded path failed); no simulation evidence changed. Automatic wrapper only ran summary, contrary to prior handover prediction; inspections performed manually now.
Trait wins/24, control→candidate: Fortification13→7; Dread5→11; Efficient6→11; War6→8; Industrial7→8; Void11→9; Swift9→10; Martial9→8; Salvagers9→8; Endurance7→8; Siege7→5; Mobile7→3. Spread remains33.33pp, fails25pp. Mobile loses five prior wins, gains one; decline occurs both map families and all seats. Do not infer cause from unchanged Mobile rule or single aggregate result.
Median55Cycles unchanged;mean55.21→56.88;50–100Cycles60→64/96;31shorter,1longer(max118). Supply deficit exposure5.19→5.23%,Manpower4.10→3.94%;entries436→460;zero own-order deficits. Ground6843→7057,naval687→695,bombard871→776. All routes retained, no claim humanwinprediction.
Construction active/starts: Tender1/12→5/23;SystemDefence2/16→3/19;SystemRepair4/28→11/74;no Militia starts. Carrier19/58→18/53;SiegePlatform26/113→22/114. Never-active spend4014/14057→4236/13715 (~28.6→30.9%). Price cuts improve uptake but not overall delivery. No final construction signoff.
Recommendation: retain package as current candidate, not approved baseline; inspect paired Mobile losses26,40,50,61,74 and Siege losses9,75,84 plus failed repair investments before selecting a coordinated corrective package. No new batch or rule edits started. Full causal/decision audit is not complete. Frozen baseline and Dessica unchanged.

## 3 October 2026 — full coordinated-package inspection and runtime requirement
Full report: release-package-study-20261003/Full_Release_Inspection_2026-10-03.txt. New evidence: deep-review-evidence.json, review-details.json, decision-review.json. All twelve trait/economy/construction aggregates reviewed, eight paired lost-win histories inspected; all five Mobile candidate traces replayed with digest checks and legal-decision probes. Confirmed mobile retreat requires an existing safe yard:12 outnumbered decisions had safe legal destinations but no safe yards;10 chose none. Do not buff Mobile blindly before correcting this. System Repair34 unfinished,24 atIntegrity1; price cuts alone do not solve delivery. No new rules or bots implemented; no batch started. Frozen study and29-file accepted baseline verified intact.
User clarified: EACH COMPLETE FUTURE BATCH <=1hour including validation. NOT stages of a larger study. Future_Balance_Batch_Policy_2026-10-03.txt supersedes all older96-game/multi-hour defaults; Future_One_Hour_Batch_Template.json defines24 new games,24 exact-reference comparisons,6 appearances/trait,2/seat,12eachmap. Current first24 took27.29minutes with replay; target35–50minutes total, acknowledge uncertainty and smaller-sample limits. No automatic further stages, timers or reminders. Do not claim six appearances establish precise win-rate convergence. Any next batch requires its own justified authorization/scope; frozen prior evidence and Dessica remain unchanged.

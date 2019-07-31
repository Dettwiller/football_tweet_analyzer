from cfb_data import SEC, week_2_opponents, week_3_opponents, week_4_opponents, week_5_opponents, week_6_opponents
from cfb_data import week_8_opponents, week_10_opponents, week_12_opponents, week_13_opponents
import matchup

#game_time = [month, day, hour, minute]
#Week 2
'''
MSU_v_KState = matchup.Matchup("MSU_v_KState", week_2_opponents["Kansas State"], SEC["Mississippi State"], [9, 8, 11, 0])
UN_v_Vandy = matchup.Matchup("UN_v_Vandy", SEC["Vanderbilt"], week_2_opponents["Nevada"], [9, 8, 11, 0])
ASU_v_UA = matchup.Matchup("ASU_v_UA", SEC["Alabama"], week_2_opponents["Arkansas State"], [9, 8, 14, 30])
UGA_v_USC = matchup.Matchup("UGA_v_USC", SEC["South Carolina"], SEC["Georgia"], [9, 8, 14, 30])
SIU_v_OM = matchup.Matchup("SIU_v_OM", SEC["Ole Miss"], week_2_opponents["Southern Illinois"], [9, 8, 15, 0])
ETSU_v_UT = matchup.Matchup("ETSU_v_UT", SEC["Tennessee"], week_2_opponents["ETSU"], [9, 8, 15, 0])
C_v_TAMU = matchup.Matchup("C_v_TAMU", SEC["Texas A&M"], week_2_opponents["Clemson"], [9, 8, 18, 0])
SELA_v_LSU = matchup.Matchup("SELA_v_LSU", SEC["LSU"], week_2_opponents["Southeastern Louisiana"], [9, 8, 18, 0])
UW_v_MIZ = matchup.Matchup("UW_v_MIZ", SEC["Missouri"], week_2_opponents["Wyoming"], [9, 8, 18, 0])
ASU_v_AU = matchup.Matchup("ASU_v_AU", SEC["Auburn"], week_2_opponents["Alabama State"], [9, 8, 18, 30])
Ark_v_CSU = matchup.Matchup("Ark_v_CSU", week_2_opponents["Colorado State"], SEC["Arkansas"], [9, 8, 18, 30])
UK_v_UF = matchup.Matchup("UK_v_UF", SEC["Florida"], SEC["Kentucky"], [9, 8, 18, 30])

week_2_matchups = [MSU_v_KState, UN_v_Vandy, ASU_v_UA, UGA_v_USC, SIU_v_OM, ETSU_v_UT, C_v_TAMU, SELA_v_LSU, UW_v_MIZ, ASU_v_AU, Ark_v_CSU, UK_v_UF]

MS_v_UK = matchup.Matchup("MS_v_UK", SEC["Kentucky"], week_3_opponents["Murray State"], [9, 15, 11, 0])
UTEP_v_UT = matchup.Matchup("UTEP_v_UT", SEC["Tennessee"], week_3_opponents["UTEP"], [9, 15, 11, 0])
V_v_ND = matchup.Matchup("V_v_ND", week_3_opponents["Notre Dame"], SEC["Vanderbilt"], [9, 15, 13, 30])
LSU_v_AU = matchup.Matchup("LSU_v_AU", SEC["Auburn"], SEC["LSU"], [9, 15, 14, 30])
CSU_v_UF = matchup.Matchup("CSU_v_UF", SEC["Florida"], week_3_opponents["Colorado State"], [9, 15, 15, 0])
UNT_v_ARK = matchup.Matchup("UNT_v_ARK", SEC["Arkansas"], week_3_opponents["North Texas"], [9, 15, 15, 0])
UA_v_OM = matchup.Matchup("UA_v_OM", SEC["Ole Miss"], SEC["Alabama"], [9, 15, 18, 0])
MTSU_v_UGA = matchup.Matchup("MTSU_v_UGA", SEC["Georgia"], week_3_opponents["Middle Tennessee"], [9, 15, 18, 15])
ULL_v_MSU = matchup.Matchup("ULL_v_MSU", SEC["Mississippi State"], week_3_opponents["Louisiana"], [9, 15, 18, 30])
ULM_v_TAMU = matchup.Matchup("ULM_v_TAMU", SEC["Texas A&M"], week_3_opponents["UL Monroe"], [9, 15, 18, 30])
MIZ_v_P = matchup.Matchup("MIZ_v_P", week_3_opponents["Purdue"], SEC["Missouri"], [9, 15, 18, 30])
WAM_v_SCAR = matchup.Matchup("WAM_v_SCAR", SEC["South Carolina"], week_3_opponents["Marshall"], [9, 15, 18, 30])

week_3_matchups = [MS_v_UK, UTEP_v_UT, V_v_ND, LSU_v_AU, CSU_v_UF, UNT_v_ARK, UA_v_OM, MTSU_v_UGA, ULL_v_MSU, ULM_v_TAMU, MIZ_v_P, WAM_v_SCAR]

UGA_v_MIZ = matchup.Matchup("UGA_v_MIZ", SEC["Missouri"], SEC["Georgia"], [9, 22, 11, 0])
KS_v_OM = matchup.Matchup("KS_v_OM", SEC["Ole Miss"], week_4_opponents["Kent State"], [9, 22, 11, 0])
TAMU_v_UA = matchup.Matchup("TAMU_v_UA", SEC["Alabama"], SEC["Texas A&M"], [9, 22, 14, 30])
SCAR_v_V = matchup.Matchup("SCAR_v_V", SEC["Vanderbilt"], SEC["South Carolina"], [9, 22, 15, 0])
LAT_v_LSU = matchup.Matchup("LAT_v_LSU", SEC["LSU"], week_4_opponents["LA Tech"], [9, 22, 18, 0])
MSU_v_UK = matchup.Matchup("MSU_v_UK", SEC["Kentucky"], SEC["Mississippi State"], [9, 22, 18, 0])
UF_v_UT = matchup.Matchup("UF_v_UT", SEC["Tennessee"], SEC["Florida"], [9, 22, 18, 0])
ARK_v_AU = matchup.Matchup("ARK_v_AU", SEC["Auburn"], SEC["Arkansas"], [9, 22, 18, 30])

week_4_matchups = [UGA_v_MIZ, KS_v_OM, TAMU_v_UA, SCAR_v_V, LAT_v_LSU, MSU_v_UK, UF_v_UT, ARK_v_AU]

UT_v_UGA = matchup.Matchup("UT_v_UGA", SEC["Georgia"], SEC["Tennessee"], [9, 29, 15, 30])
ULL_v_UA = matchup.Matchup("ULL_v_UA", SEC["Alabama"], week_5_opponents["Louisiana"], [9, 29, 11, 0])
ARK_v_TAMU = matchup.Matchup("ARK_v_TAMU", SEC["Texas A&M"], SEC["Arkansas"], [9, 29, 11, 0])
USM_v_AU = matchup.Matchup("USM_v_AU", SEC["Auburn"], week_5_opponents["Southern Miss"], [9, 29, 15, 0])
TSU_v_V = matchup.Matchup("TSU_v_V", SEC["Vanderbilt"], week_5_opponents["Tennessee State"], [9, 29, 15, 0])
UF_v_MSU = matchup.Matchup("UF_v_MSU", SEC["Mississippi State"], SEC["Florida"], [9, 29, 17, 0])
SCAR_v_UK = matchup.Matchup("SCAR_v_UK", SEC["Kentucky"], SEC["South Carolina"], [9, 29, 18, 30])
OM_v_LSU = matchup.Matchup("OM_v_LSU", SEC["LSU"], SEC["Ole Miss"], [9, 29, 20, 0])

week_5_matchups = [UT_v_UGA, ULL_v_UA, ARK_v_TAMU, USM_v_AU, TSU_v_V, UF_v_MSU, SCAR_v_UK, OM_v_LSU]


UA_v_ARK = matchup.Matchup("UA_v_ARK", SEC["Arkansas"], SEC["Alabama"], [10, 6, 11, 0])
MIZ_v_SCAR = matchup.Matchup("MIZ_v_SCAR", SEC["South Carolina"], SEC["Missouri"], [10, 6, 11, 0])
LSU_v_UF = matchup.Matchup("LSU_v_UF", SEC["Florida"], SEC["LSU"], [10, 6, 13, 30])
ULM_v_OM = matchup.Matchup("ULM_v_OM", SEC["Ole Miss"], week_6_opponents["UL Monroe"], [10, 6, 14, 0])
UK_v_TAMU = matchup.Matchup("UK_v_TAMU", SEC["Texas A&M"], SEC["Kentucky"], [10, 6, 17, 0])
AU_v_MSU = matchup.Matchup("AU_v_MSU", SEC["Mississippi State"], SEC["Auburn"], [10, 6, 17, 30])
V_v_UGA = matchup.Matchup("V_v_UGA", SEC["Georgia"], SEC["Vanderbilt"], [10, 6, 17, 30])

week_6_matchups = [UA_v_ARK, MIZ_v_SCAR, LSU_v_UF, ULM_v_OM, UK_v_TAMU, AU_v_MSU, V_v_UGA]


UF_v_V = matchup.Matchup("UF_v_V", SEC["Vanderbilt"], SEC["Florida"], [10, 13, 11, 0])
UT_v_AU = matchup.Matchup("UT_v_AU", SEC["Auburn"], SEC["Tennessee"], [10, 13, 11, 0])
UGA_v_LSU = matchup.Matchup("UGA_v_LSU", SEC["LSU"], SEC["Georgia"], [10, 13, 14, 30])
TAMU_v_SCAR = matchup.Matchup("TAMU_v_SCAR", SEC["South Carolina"], SEC["Texas A&M"], [10, 13, 14, 30])
MIZ_v_UA = matchup.Matchup("MIZ_v_UA", SEC["Alabama"], SEC["Missouri"], [10, 13, 18, 0])
OM_v_ARK = matchup.Matchup("OM_v_ARK", SEC["Arkansas"], SEC["Ole Miss"], [10, 13, 18, 30])

week_7_matchups = [UF_v_V, UT_v_AU, UGA_v_LSU, TAMU_v_SCAR, MIZ_v_UA, OM_v_ARK]


AU_v_OM = matchup.Matchup("AU_v_OM", SEC["Ole Miss"], SEC["Auburn"], [10, 20, 11, 0])
TU_v_ARK = matchup.Matchup("TU_v_ARK", SEC["Arkansas"], week_8_opponents["Tulsa"], [10, 20, 11, 0])
UA_v_UT = matchup.Matchup("UA_v_UT", SEC["Tennessee"], SEC["Alabama"], [10, 20, 14, 30])
MEM_v_MIZ = matchup.Matchup("MEM_v_MIZ", SEC["Missouri"], week_8_opponents["Memphis"], [10, 20, 15, 0])
MSU_v_LSU = matchup.Matchup("MSU_v_LSU", SEC["LSU"], SEC["Mississippi State"], [10, 20, 18, 0])
V_v_UK = matchup.Matchup("V_v_UK", SEC["Kentucky"], SEC["Vanderbilt"], [10, 20, 18, 30])

week_8_matchups = [AU_v_OM, TU_v_ARK, UA_v_UT, MEM_v_MIZ, MSU_v_LSU, V_v_UK]


V_v_ARK = matchup.Matchup("V_v_ARK", SEC["Arkansas"], SEC["Vanderbilt"], [10, 27, 11, 0])
UF_v_UGA = matchup.Matchup("UF_v_UGA", SEC["Georgia"], SEC["Florida"], [10, 27, 14, 30])
UK_v_MIZ = matchup.Matchup("UK_v_MIZ", SEC["Missouri"], SEC["Kentucky"], [10, 27, 15, 0])
TAMU_v_MSU = matchup.Matchup("TAMU_v_MSU", SEC["Mississippi State"], SEC["Texas A&M"], [10, 27, 18, 0])
UT_v_SCAR = matchup.Matchup("UT_v_SCAR", SEC["South Carolina"], SEC["Tennessee"], [10, 27, 18, 30])

week_9_matchups = [V_v_ARK, UF_v_UGA, UK_v_MIZ, TAMU_v_MSU, UT_v_SCAR]


TAMU_v_AU = matchup.Matchup("TAMU_v_AU", SEC["Auburn"], SEC["Texas A&M"], [11, 3, 11, 0])
SCAR_v_OM = matchup.Matchup("SCAR_v_OM", SEC["Ole Miss"], SEC["South Carolina"], [11, 3, 11, 0])
UGA_v_UK = matchup.Matchup("UGA_v_UK", SEC["Kentucky"], SEC["Georgia"], [11, 3, 14, 30])
MIZ_v_UF = matchup.Matchup("MIZ_v_UF", SEC["Florida"], SEC["Missouri"], [11, 3, 15, 0])
CHAR_v_UT = matchup.Matchup("CHAR_v_UT", SEC["Tennessee"], week_10_opponents["Charlotte"], [11, 3, 15, 0])
LAT_v_MSU = matchup.Matchup("LAT_v_MSU", SEC["Mississippi State"], week_10_opponents["LA Tech"], [11, 3, 18, 30])
UA_v_LSU = matchup.Matchup("UA_v_LSU", SEC["LSU"], SEC["Alabama"], [11, 3, 19, 0])

week_10_matchups = [TAMU_v_AU, SCAR_v_OM, UGA_v_UK, MIZ_v_UF, CHAR_v_UT, LAT_v_MSU, UA_v_LSU]


SCAR_v_UF = matchup.Matchup("SCAR_v_UF", SEC["Florida"], SEC["South Carolina"], [11, 10, 11, 0])
OM_v_TAMU = matchup.Matchup("OM_v_TAMU", SEC["Texas A&M"], SEC["Ole Miss"], [11, 10, 11, 0])
V_v_MIZ = matchup.Matchup("V_v_MIZ", SEC["Missouri"], SEC["Vanderbilt"], [11, 10, 11, 0])
MSU_v_UA = matchup.Matchup("MSU_v_UA", SEC["Alabama"], SEC["Mississippi State"], [11, 10, 14, 30])
UK_v_UT = matchup.Matchup("UK_v_UT", SEC["Tennessee"], SEC["Kentucky"], [11, 10, 14, 30])
AU_v_UGA = matchup.Matchup("AU_v_UGA", SEC["Georgia"], SEC["Auburn"], [11, 10, 18, 0])
LSU_v_ARK = matchup.Matchup("LSU_v_ARK", SEC["Arkansas"], SEC["LSU"], [11, 10, 18, 30])

week_11_matchups = [SCAR_v_UF, OM_v_TAMU, V_v_MIZ, MSU_v_UA, UK_v_UT, AU_v_UGA, LSU_v_ARK]


CIT_v_UA = matchup.Matchup("CIT_v_UA", SEC["Alabama"], week_12_opponents["The Citadel"], [11, 17, 11, 0])
MTS_v_UK = matchup.Matchup("MTS_v_UK", SEC["Kentucky"], week_12_opponents["Middle Tennessee"], [11, 17, 11, 0])
I_v_UF = matchup.Matchup("I_v_UF", SEC["Florida"], week_12_opponents["Idaho"], [11, 17, 11, 0])
ARK_v_MSU = matchup.Matchup("ARK_v_MSU", SEC["Mississippi State"], SEC["Arkansas"], [11, 17, 11, 0])
MIZ_v_UT = matchup.Matchup("MIZ_v_UT", SEC["Tennessee"], SEC["Missouri"], [11, 17, 14, 30])
UMASS_v_UGA = matchup.Matchup("UMASS_v_UGA", SEC["Georgia"], week_12_opponents["UMass"], [11, 17, 15, 0])
L_v_AU = matchup.Matchup("L_v_AU", SEC["Auburn"], week_12_opponents["Liberty"], [11, 17, 15, 0])
UAB_v_TAMU = matchup.Matchup("UAB_v_TAMU", SEC["Texas A&M"], week_12_opponents["UAB"], [11, 17, 18, 0])
R_v_LSU = matchup.Matchup("R_v_LSU", SEC["LSU"], week_12_opponents["Rice"], [11, 17, 18, 30])
OM_v_V = matchup.Matchup("OM_v_V", SEC["Vanderbilt"], SEC["Ole Miss"], [11, 17, 18, 30])
CHAT_v_SCAR = matchup.Matchup("CHAT_v_SCAR", SEC["South Carolina"], week_12_opponents["Chattanooga"], [11, 17, 18, 30])

week_12_matchups = [CIT_v_UA, MTS_v_UK, I_v_UF, ARK_v_MSU, MIZ_v_UT, UMASS_v_UGA, L_v_AU, UAB_v_TAMU, R_v_LSU, OM_v_V, CHAT_v_SCAR]


MSU_v_OM = matchup.Matchup("MSU_v_OM", SEC["Ole Miss"], SEC["Mississippi State"], [11, 22, 18, 30])
ARK_v_MIZ = matchup.Matchup("ARK_v_MIZ", SEC["Missouri"], SEC["Arkansas"], [11, 23, 13, 30])
GT_v_UGA = matchup.Matchup("GT_v_UGA", SEC["Georgia"], week_13_opponents["Georgia Tech"], [11, 24, 11, 0])
UF_v_FSU = matchup.Matchup("UF_v_FSU", week_13_opponents["Florida State"], SEC["Florida"], [11, 24, 11, 0])
AU_v_UA = matchup.Matchup("AU_v_UA", SEC["Alabama"], SEC["Auburn"], [11, 24, 14, 30])
UT_v_V = matchup.Matchup("UT_v_V", SEC["Vanderbilt"], SEC["Tennessee"], [11, 24, 15, 0])
SCAR_v_C = matchup.Matchup("SCAR_v_C", week_13_opponents["Clemson"], SEC["South Carolina"], [11, 24, 18, 0])
UK_v_UL = matchup.Matchup("UK_v_UL", week_13_opponents["Louisville"], SEC["Kentucky"], [11, 24, 18, 0])
LSU_v_TAMU = matchup.Matchup("LSU_v_TAMU", SEC["Texas A&M"], SEC["LSU"], [11, 24, 18, 30])

week_13_matchups = [ MSU_v_OM, ARK_v_MIZ, GT_v_UGA, UF_v_FSU, AU_v_UA, UT_v_V, SCAR_v_C, UK_v_UL, LSU_v_TAMU]
'''

UA_v_UGA = matchup.Matchup("UA_v_UGA", SEC["Georgia"], SEC["Alabama"], [12, 1, 15, 0])
week_14_matchups = [UA_v_UGA]
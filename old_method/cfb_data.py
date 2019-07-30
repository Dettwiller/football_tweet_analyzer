import team

Alabama_tags = ["#rolltide", "#crimsontide", "#bama", "#RTR", "#alabamafootball"]
Arkansas_tags = ["#razorbacks", "#woopig", "#arkansasfootball", "#arkansasrazorbacks", "#wps", "#woopigsooie", "#gohogs", "#razorback", "#razorbackfb"]
Auburn_tags = ["#wareagle", "#auburnfootball", "#auburn"]
Florida_tags = ["#gators", "#gatorsfootball", "#floridafootball", "#uffootball", "#gogators", "#gatorsfb"]
Georgia_tags = ["#georgiafootball", "#uga", "#ugafootball", "#ugafb"]
Kentucky_tags = ["#kentuckyfootball", "#bbn", "#weareuk", "#ukfootball"]
LSU_tags = ["#LSU", "#geauxtigers", "#lsutigers", "#lsufootball"]
MississippiState_tags = ["#hailstate", "#msstate", "#mississippistate"]
Missouri_tags = ["#mizzou", "#mizzoufootball", "#missourifootball", "#miz"]
OleMiss_tags = ["#hottytoddy", "#olemiss", "#olemissfootball", "#olemissfb"]
SouthCarolina_tags = ["#gamecocks", "#gamecock", "#gamecocksfootball", "#spursup", "#southcarolinafootball", "#gogamecocks"]
Tennessee_tags = ["#vols", "#tennesseefootball", "#govols", "#poweredbythet", "#rockytop", "#gbo"]
TexasAM_tags = ["#TAMU", "#aggiefootball", "#gigem", "#TAMUfootball"]
Vanderbilt_tags = ["#anchordown", "#vandyfootball", "#vanderbiltfootball", "#vandy", "#fightdores"]

Alabama = team.Team("Alabama", Alabama_tags)
Arkansas = team.Team("Arkansas", Arkansas_tags)
Auburn = team.Team("Auburn", Auburn_tags)
Florida = team.Team("Florida", Florida_tags)
Georgia = team.Team("Georgia", Georgia_tags)
Kentucky = team.Team("Kentucky", Kentucky_tags)
LSU = team.Team("LSU", LSU_tags)
MississippiState = team.Team("Mississippi State", MississippiState_tags)
Missouri = team.Team("Missouri", Missouri_tags)
OleMiss = team.Team("Ole Miss", OleMiss_tags)
SouthCarolina = team.Team("South Carolina", SouthCarolina_tags)
Tennessee = team.Team("Tennessee", Tennessee_tags)
TexasAM = team.Team("Texas A&M", TexasAM_tags)
Vanderbilt = team.Team("Vanderbilt", Vanderbilt_tags)

SEC = {
    Alabama.name : Alabama, Arkansas.name : Arkansas, Auburn.name: Auburn, Florida.name : Florida, Georgia.name: Georgia,
    Kentucky.name: Kentucky, LSU.name : LSU, MississippiState.name : MississippiState, Missouri.name : Missouri,
    OleMiss.name : OleMiss, SouthCarolina.name : SouthCarolina, Tennessee.name : Tennessee, TexasAM.name : TexasAM,
    Vanderbilt.name : Vanderbilt
}

#week 2
KansasState_tags = ["#kansasstatefootball", "#kstate", "#kstatefootball", "#kstateFB", "#emaw"]
KansasState = team.Team("Kansas State", KansasState_tags)
Nevada_tags = ["#battleborn", "#nevadagrit", "#nevadafootball"]
Nevada = team.Team("Nevada", Nevada_tags)
ArkansasState_tags = ["#astate", "#astatefootball", "#arkansasstate", "#howlyes", "#wolvesup"]
ArkansasState = team.Team("Arkansas State", ArkansasState_tags)
SouthernIllinois_tags = ["#salukis"]
SouthernIllinois = team.Team("Southern Illinois", SouthernIllinois_tags)
ETSU_tags = ["#etsufootball", "#etsutough"]
ETSU = team.Team("ETSU", ETSU_tags)
Clemson_tags = ["#Clemson", "#clemsonfootball", "#clemsontigers"]
Clemson = team.Team("Clemson", Clemson_tags)
SoutheasternLouisiana_tags = ["#lionup"]
SoutheasternLouisiana = team.Team("Southeastern Louisiana", SoutheasternLouisiana_tags)
Wyoming_tags = ["#gowyo", "#onewyoming", "#wyosports", "#wyofootball"]
Wyoming = team.Team("Wyoming", Wyoming_tags)
AlabamaState_tags = ["#alabamastate", "#myasu", "#bamastate"]
AlabamaState = team.Team("Alabama State", AlabamaState_tags)
ColoradoState_tags = ["#CSUrams", "#coloradostate", "#csufootball"]
ColoradoState = team.Team("Colorado State", ColoradoState_tags)

week_2_opponents = {
    KansasState.name : KansasState, Nevada.name : Nevada, ArkansasState.name : ArkansasState,
    SouthernIllinois.name : SouthernIllinois, ETSU.name : ETSU, Clemson.name : Clemson,
    SoutheasternLouisiana.name : SoutheasternLouisiana, Wyoming.name : Wyoming,
    AlabamaState.name : AlabamaState, ColoradoState.name : ColoradoState
}

#week 3
MurrayState_tags = ["#murraystate", "#goracers", "#racernation"]
MurrayState = team.Team("Murray State", MurrayState_tags)
UTEP_tags = ["#utep", "#utepfootball", "#gominers", "#picksup", "#utepfb", "#minerstrong"]
UTEP = team.Team("UTEP", UTEP_tags)
NotreDame_tags = ["#notredame", "#ndfootball", "#notredamefootball", "#fightingirish", "#goirish"]
NotreDame = team.Team("Notre Dame", NotreDame_tags)
#Colorado State
NorthTexas_tags = ["#northtexasfootball", "#meangreen", "#gmg"]
NorthTexas = team.Team("North Texas", NorthTexas_tags)
MiddleTennessee_tags = ["#mtsu", "#blueraiders"]
MiddleTennessee = team.Team("Middle Tennessee", MiddleTennessee_tags)
Louisiana_tags = ["geauxcajuns"]
Louisiana = team.Team("Louisiana", Louisiana_tags)
ULMonroe_tags = ["#ulmfootball", "#defendthenest", "#ulmwarhawks", "#talonsout"]
ULMonroe = team.Team("UL Monroe", ULMonroe_tags)
Purdue_tags = ["#purdue", "#boilerup", "#boilerfootball", "#purduefootball"]
Purdue = team.Team("Purdue", Purdue_tags)
Marshall_tags = ["#thunderingherd", "#goherd", "#wearemarshall"]
Marshall = team.Team("Marshall", Marshall_tags)

week_3_opponents = {
    MurrayState.name : MurrayState, UTEP.name : UTEP, NotreDame.name : NotreDame,
    ColoradoState.name : ColoradoState, NorthTexas.name : NorthTexas,
    MiddleTennessee.name : MiddleTennessee, Louisiana.name : Louisiana,
    ULMonroe.name : ULMonroe, Purdue.name : Purdue, Marshall.name : Marshall
}

#week 4
LaTech_tags = ["#latech", "#everloyalbe"]
LaTech = team.Team("LA Tech", LaTech_tags)
KentState_tags = ["#kentst", "#kentstate", "#goldenflashes", "#goflashes"]
KentState = team.Team("Kent State", KentState_tags)

week_4_opponents = {LaTech.name : LaTech, KentState.name : KentState}

#week 5
#Louisiana
SouthernMiss_tags = ["#SouthernMiss", "#smttt", "#usmfootball"]
SouthernMiss = team.Team("Southern Miss", SouthernMiss_tags)
TennesseeState_tags = ["#tnstate", "#bigbluerising"]
TennesseeState = team.Team("Tennessee State", TennesseeState_tags)

week_5_opponents = {
    Louisiana.name : Louisiana, SouthernMiss.name : SouthernMiss,
    TennesseeState.name : TennesseeState
}

#week 6
#UL Monroe
week_6_opponents = {ULMonroe.name : ULMonroe}

#week 8
Tulsa_tags = ["#tulsahurricane", "#goldenhurricane", "#reigncane", "#tulsafb"]
Tulsa = team.Team("Tulsa", Tulsa_tags)
Memphis_tags = ["#gotigersgo", "#stripeup", "#memphistigers", "#gtg"]
Memphis = team.Team("Memphis", Memphis_tags)

week_8_opponents = {Tulsa.name : Tulsa, Memphis.name : Memphis}


#week 10
#La Tech
Charlotte_tags = ["#uncc", "#unccharlotte"]
Charlotte = team.Team("Charlotte", Charlotte_tags)

week_10_opponents = {LaTech.name : LaTech, Charlotte.name : Charlotte}

#week 12
TheCitadel_tags = ["#firethosecannons", "#citadelstrength", "#citadelfootball"]
TheCitadel = team.Team("The Citadel", TheCitadel_tags)
UMass_tags = ["#unitethemasses", "#umass", "#umassfootball", "#flagship"]
UMass = team.Team("UMass", UMass_tags)
Liberty_tags = ["#libertyfootball", "#goflames"]
Liberty = team.Team("Liberty", Liberty_tags)
Rice_tags = ["#riceowls", "#goowls", "#ricefb", "#ricefootball"]
Rice = team.Team("Rice", Rice_tags)
Idaho_tags = ["#govandals", "#idahofootball"]
Idaho = team.Team("Idaho", Idaho_tags)
#Middle Tennessee
Chattanooga_tags = ["#mocs", "#gomocs", "#utcfootball"]
Chattanooga = team.Team("Chattanooga", Chattanooga_tags)
UAB_tags = ["#uab", "#goblazers", "#uabfootball", "#winasone"]
UAB = team.Team("UAB", UAB_tags)

week_12_opponents = {
    TheCitadel.name : TheCitadel, UMass.name : UMass, Liberty.name : Liberty,
    Rice.name : Rice, Idaho.name : Idaho, MiddleTennessee.name : MiddleTennessee,
    Chattanooga.name : Chattanooga, UAB.name : UAB
}

#week 13
GeorgiaTech_tags = ["#togetherweswarm", "#gatech"]
GeorgiaTech = team.Team("Georgia Tech", GeorgiaTech_tags)
FloridaState_tags = ["#seminoles", "#noles", "#fsufootball", "#fsu", "#gonoles", "#nolesfb", "#nolesfootball"]
FloridaState = team.Team("Florida State", FloridaState_tags)
Louisville_tags = ["#louisvillefootball", "#uofl", "#uoflfootball", "#L1C4"]
Louisville = team.Team("Louisville", Louisville_tags)

week_13_opponents = { GeorgiaTech.name : GeorgiaTech, FloridaState.name : FloridaState, Louisville.name : Louisville, Clemson.name: Clemson}
\ Model EI
\ LP format - for model browsing. Use MPS format to capture full model detail.
Maximize
  teamvars[DrawChange] + teamvars[AgapeYouthandFamilyCenter]
   + teamvars[AfricaHouse] + teamvars[Southface] + teamvars[CampKudzu]
   + teamvars[LaAmistad] + teamvars[GivingKitchen] + teamvars[WonderRoot]
   + teamvars[Rebuilding] + -0 membervars['RosemarieHunt']
   + -0 membervars['PauletteMartin'] + -0 membervars['AlbertGross']
   + -0 membervars['AustinWatts'] + -0 membervars['SherryHarrington']
   + -0 membervars['EdwinChambers'] + -0 membervars['JennyKelley']
   + -0 membervars['DarrinRuiz'] + -0 membervars['DebraIngram']
   + -0 membervars['LutherNorman'] + -0 membervars['ToddQuinn']
   + -0 membervars['MaureenHudson'] + -0 membervars['KristinaHines']
   + -0 membervars['FredaDaniels'] + -0 membervars['TraciRivera']
   + -0 membervars['SamJohnson'] + -0 membervars['LillianOliver']
   + -0 membervars['MeganWallace'] + -0 membervars['VioletMclaughlin']
   + -0 membervars['KristinHubbard'] + -0 membervars['KennyMorales']
   + -0 membervars['ThomasWest'] + -0 membervars['SheilaMay']
   + -0 membervars['CraigTerry'] + -0 membervars['DebbieMcgee']
   + -0 membervars['DoyleFrank'] + -0 membervars['VirgilGraves']
   + -0 membervars['AnneVaughn'] + -0 membervars['RudyBush']
   + -0 membervars['BerthaAllen'] + -0 membervars['LindsayPatrick']
   + -0 membervars['JuliusCraig'] + -0 membervars['JessieMoreno']
   + -0 membervars['MelindaPayne'] + -0 membervars['GeraldineLawson']
   + -0 membervars['DerrickSwanson'] + -0 membervars['LorraineDelgado']
   + -0 membervars['GraceEstrada'] + -0 membervars['JonathanRiley']
   + -0 membervars['MauriceCobb'] + -0 membervars['ZacharySandoval']
   + -0 membervars['ChristinaAlvarez'] + -0 membervars['KelleyBanks']
   + -0 membervars['DianeWalton'] + -0 membervars['JaneJackson']
   + -0 membervars['EdHamilton'] + -0 membervars['LyleJoseph']
   + -0 membervars['CynthiaWebb'] + -0 membervars['KendraRodriguez']
   + -0 membervars['SueHerrera'] + -0 membervars['NancyPark']
   + -0 membervars['TerranceMack'] + -0 membervars['LoriGutierrez']
   + -0 membervars['LyndaBrown'] + -0 membervars['WillieGregory']
   + -0 membervars['JasonCortez'] + -0 membervars['DelbertParks']
   + -0 membervars['AmandaParsons'] + -0 membervars['DonaldMann']
   + -0 membervars['GwendolynClarke'] + -0 membervars['OllieMendoza']
   + -0 membervars['JuanaWilson'] + -0 membervars['GeoffreyHarvey']
   + -0 membervars['SaulThompson'] + -0 membervars['RandolphMarshall']
   + -0 membervars['GingerCampbell']
Subject To
 maxmembers: teamvars[DrawChange] <= 10
 maxmembers: teamvars[AgapeYouthandFamilyCenter] <= 10
 maxmembers: teamvars[AfricaHouse] <= 10
 maxmembers: teamvars[Southface] <= 10
 maxmembers: teamvars[CampKudzu] <= 10
 maxmembers: teamvars[LaAmistad] <= 10
 maxmembers: teamvars[GivingKitchen] <= 10
 maxmembers: teamvars[WonderRoot] <= 10
 maxmembers: teamvars[Rebuilding] <= 10
Bounds
 teamvars[DrawChange] >= -999
 teamvars[AgapeYouthandFamilyCenter] >= -999
 teamvars[AfricaHouse] >= -999
 teamvars[Southface] >= -999
 teamvars[CampKudzu] >= -999
 teamvars[LaAmistad] >= -999
 teamvars[GivingKitchen] >= -999
 teamvars[WonderRoot] >= -999
 teamvars[Rebuilding] >= -999
Binaries
 membervars['RosemarieHunt'] membervars['PauletteMartin']
 membervars['AlbertGross'] membervars['AustinWatts']
 membervars['SherryHarrington'] membervars['EdwinChambers']
 membervars['JennyKelley'] membervars['DarrinRuiz']
 membervars['DebraIngram'] membervars['LutherNorman']
 membervars['ToddQuinn'] membervars['MaureenHudson']
 membervars['KristinaHines'] membervars['FredaDaniels']
 membervars['TraciRivera'] membervars['SamJohnson']
 membervars['LillianOliver'] membervars['MeganWallace']
 membervars['VioletMclaughlin'] membervars['KristinHubbard']
 membervars['KennyMorales'] membervars['ThomasWest']
 membervars['SheilaMay'] membervars['CraigTerry'] membervars['DebbieMcgee']
 membervars['DoyleFrank'] membervars['VirgilGraves']
 membervars['AnneVaughn'] membervars['RudyBush'] membervars['BerthaAllen']
 membervars['LindsayPatrick'] membervars['JuliusCraig']
 membervars['JessieMoreno'] membervars['MelindaPayne']
 membervars['GeraldineLawson'] membervars['DerrickSwanson']
 membervars['LorraineDelgado'] membervars['GraceEstrada']
 membervars['JonathanRiley'] membervars['MauriceCobb']
 membervars['ZacharySandoval'] membervars['ChristinaAlvarez']
 membervars['KelleyBanks'] membervars['DianeWalton']
 membervars['JaneJackson'] membervars['EdHamilton']
 membervars['LyleJoseph'] membervars['CynthiaWebb']
 membervars['KendraRodriguez'] membervars['SueHerrera']
 membervars['NancyPark'] membervars['TerranceMack']
 membervars['LoriGutierrez'] membervars['LyndaBrown']
 membervars['WillieGregory'] membervars['JasonCortez']
 membervars['DelbertParks'] membervars['AmandaParsons']
 membervars['DonaldMann'] membervars['GwendolynClarke']
 membervars['OllieMendoza'] membervars['JuanaWilson']
 membervars['GeoffreyHarvey'] membervars['SaulThompson']
 membervars['RandolphMarshall'] membervars['GingerCampbell']
End

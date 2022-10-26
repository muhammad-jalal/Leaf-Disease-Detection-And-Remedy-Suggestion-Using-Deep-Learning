from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/')
def main():
    person = {'data': [
{'discription':"Apple scab is caused by a fungus, Venturia inaequalis, and is a serious disease of apple and crabapple (genus Malus) trees that spreads quickly and easily. Generally, you’ll first notice it in early spring, when rains, wind, and cool temperatures spread the fungal spores.",
'name':"Apple___Apple_scab",
'remedy':["1.     Grow scab-resistant cultivars of apples. Apples with good resistance include Akane, Chehalis, Liberty, Prima and Tydeman Red.",
"2.Apply nitrogen to leaves that have fallen to the ground in the fall to enhance decomposition of fallen leaves and make them more palatable to earthworms. Hand apply a liquid fish solution or 16-16-16 fertilizer to help with the decomposition.",
"3.Shred fallen leaves in the fall with a mower to help speed up decomposition.",
"4.Prune your apple trees to open up branching and allow more air circulation.",
"5.When watering your apple trees, avoid getting foliage wet.",
"6.Apply dolomitic lime in the fall, after leaf drop, to increase pH and to help reduce fungal spores in the spring.",
"7.Spray fungicide – Bonide Captan, wettable sulfur, summer lime sulfur or Spectracide Immunox – when temperatures are above 60 degrees and the leaves or blooms are wet."
]},

{
'discription':"Black rot is a disease of apples that infects fruit, leaves, and bark caused by the fungus Botryosphaeria obtusa. It can also jump to healthy tissue on pear or quince trees but is typically a secondary fungus of weak or dead tissues in other plants.",
'name':"Apple___Black_rot",
'remedy':["1.Prune out dead or diseased branches.",
"2.Pick all dried and shriveled fruits remaining on the trees.",
"3.Remove infected plant material from the area.",
"4.All infected plant parts should be burned, buried or sent to a municipal composting site.",
"5.Be sure to remove the stumps of any apple trees you cut down. Dead stumps can be a source of spores."
]
},


{
'discription':"Cedar apple rust (Gymnosporangium juniperi-virginianae) is a fungal disease that requires juniper plants to complete its complicated two year life-cycle. Spores overwinter as a reddish-brown gall on young twigs of various juniper species. In early spring, during wet weather, these galls swell and bright orange masses of spores are blown by the wind where they infect susceptible apple and crab-apple trees.",
'name':"Apple___Cedar_apple_rust",
'remedy':["1.Choose resistant cultivars when available.",
"2.Rake up and dispose of fallen leaves and other debris from under trees.",
"3.Remove galls from infected junipers. In some cases, juniper plants should be removed entirely.",
"4.Apply preventative, disease-fighting fungicides labeled for use on apples weekly, starting with bud break, to protect trees from spores being released by the juniper host. This occurs only once per year, so additional applications after this springtime spread are not necessary.",
"5.On juniper, rust can be controlled by spraying plants with a copper solution (0.5 to 2.0 oz/ gallon of water) at least four times between late August and late October.",
"6.Containing sulfur and pyrethrins, one-hit concentrate for insect attacks and fungal problems. For best results, apply as a protective spray (2.5 oz/ gallon) early in the season. If disease, insects or wet weather are present, mix 5 oz in one gallon of water. Thoroughly spray all parts of the plant, especially new shoots.",
"7.Contact your local Agricultural Extension office for other possible solutions in your area."
]
},
{'discription':"It's a healthy leaf",
'name':"Apple_healthy",
'remedy':["Maintain the plant"]
},
{'discription':"It's a healthy leaf",
'name':"Cherry_healthy",
'remedy':["Maintain the plant"]},

{
'discription':"Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, an obligate biotrophic fungus. Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface.",
'name':"Cherry_(including_sour)___Powdery_mildew",
'remedy':["1.Plant resistant cultivars in sunny locations whenever possible.",
"2.Prune or stake plants to improve air circulation. Make sure to disinfect your pruning tools (one part bleach to 4 parts water) after each cut.",
"3.Remove diseased foliage from the plant and clean up fallen debris on the ground.",
"4.Use a thick layer of mulch or organic compost to cover the soil after you have raked and cleaned it well. Mulch will prevent the disease spores from splashing back up onto the leaves.",
"5.Milk sprays, made with 40% milk and 60% water, are an effective home remedy for use on a wide range of plants. For best results, spray plant leaves as a preventative measure every 10-14 days.",
"6.Wash foliage occasionally to disrupt the daily spore-releasing cycle. Neem oil and PM Wash, used on a 7 day schedule, will prevent fungal attack on plants grown indoors.",
"7.Water in the morning, so plants have a chance to dry during the day. Drip irrigation and soaker hoses will help keep the foliage dry.",
"8.Use a slow-release, organic fertilizer on crops and avoid excess nitrogen. Soft, leafy, new growth is most susceptible.",
"9.Destroy all plant debris after harvest. Do NOT compost."
]
},


{
'discription':"Gray leaf spot (GLS) is a common fungal disease caused by the pathogen Cercospora zeae-maydis in corn.Disease development is favored by warm temperatures, 80°F or 27 °C; and high humidity, relative humidity of 90% or higher for 12 hours or more.Cercospora zeae-maydis overwinters in corn residue, allowing inoculum to build up from year to year in fields.Cropping systems with reduced- or no-till and/or continuous corn are at higher risk for gray leaf spot outbreaks.Conducive weather conditions encourage the rapid spread of disease near the end of summer and early fall, when corn plants allocate more resources to grainfill.",
'name':"Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
'remedy':["1.Cercospora zeae-maydis overwinters in corn debris, so production practices such as tillage and crop rotation that reduce the amount corn residue on the surface will decrease the amount of primary inoculum.",
"2.Crop rotation away from corn can reduce disease pressure, but multiple years may be necessary in no-till scenarios.",
"3.Planting hybrids with a high level of genetic resistance can help reduce the risk of yield loss due to gray leaf spot infection.",
"4.During the growing season, foliar fungicides can be used to manage gray leaf spot outbreaks.",
"5.Farmers must consider the cost of the application and market value of their corn before determining if fungicides will be an economical solution to GLS."
]
},


{
'discription':"Common corn rust, caused by the fungus Puccinia sorghi,It rarely reaches levels that cause yield loss in commercial hybrids. It is most problematic during prolonged periods of cool, wet weather. Rust diseases are generally easy to identify by the appearance of brown pustules.",
'name':"Corn_(maize)___Common_rust_",
'remedy':["1.Maize rusts are generally controlled by the use of resistant maize hybrids, and by foliar applications of fungicides on sweet corn. Cultural practices may be effective in areas where rust spores can overwinter on debris or where infected Oxalis species are a source of spores. Therefore, collect the remains of the crop and destroy by burning or burying, and weed around maize plots if Oxalis is common. Destroy 'volunteer' maize plants before planting new crops.",
"2.The use of resistant varieties is the best way of managing rust diseases. Two types of resistance exist: partial resistant and qualitative resistance. Partial resistance (or tolerance) results in fewer pustules, reduced sporulation, and lower germination rates. Disease spread and the development of epidemics are slower. Qualitative resistance is based on single genes providing total resistance. The trouble with this kind of resistance is that it may encourage the selection of new strains of the rust that can overcome varietal resistance.",
"3.Fungicides have been used against both common and southern rust, but they are usually not needed in maize because of the resistance bred into commercial varieties. However, foliar fungicides may have a use on sweet corn. A number of protectant fungicide have been recommended: e.g., chlorothalonil and mancozeb. Plants are monitored and sprays commence when there are on average six pustules per leaf."
]
},
{'discription':"It's a healthy leaf",
'name':"Corn_healthy",
'remedy':["Maintain the plant"]},

{
'discription':"Northern corn leaf blight (NCLB) or Turcicum leaf blight (TLB) is a foliar disease of corn (maize) caused by Exserohilum turcicum, the anamorph of the ascomycete Setosphaeria turcica. With its characteristic cigar-shaped lesions, this disease can cause significant yield loss in susceptible corn hybrids.",
'name':"Corn_(maize)___Northern_Leaf_Blight",
'remedy':["1.Management of NCLB can be achieved primarily by using hybrids with resistance, but because resistance may not be complete or may fail, it is advantageous to utilize an integrated approach with different cropping practices and fungicides. Scouting fields and monitoring local conditions is vital to control this disease.",
"2.Ways to change cropping practices to control the disease include reducing the amount of infected residue left in a field, managing weeds to improve airflow and reduce humidity, and encouraging residue decomposition with tillage. The tillage will assist in breaking down crop debris and reducing existing inoculum.",
"3.The use of foliar fungicides for corn have also been shown to control NCLB.[5] Research suggests that using fungicides to keep the upper 75% of the leaf canopy disease-free for three quarters of the grain-filling period will eliminate yield loss [11] To ensure that newly emerging leaf tissue is protected from infection, before the plants are in tassel, fungicides should be applied on the same day that significant conidial dispersal is expected to occur."
]
},


{
'discription':"Grape black rot is a fungal disease caused by an ascomycetous fungus, Guignardia bidwellii, that attacks grape vines during hot and humid weather.It can cause complete crop loss in warm, humid climates, but is virtually unknown in regions with arid summers.The disease also attacks other parts of the plant,The most damaging effect is to the fruit.",
'name':"Grape Black Rot",
'remedy':["1.The first control method is to choose the right grape cultivar for the region that the grape will be grown in.Grape cultivars differ in their susceptibility to diseases, including differences in the disease black rot.Some varieties are less susceptible, while others are more prone to the disease when the right environmental conditions occur.",
"2.A proper pruning technique is another cultural control method to limit diseases.Prune each vine every year during the dormant period.This dormant pruning is heavily researched to provide the term-balanced pruning.",
"3.The last cultural control method would be to maintain clean fields once infected.Keep the field well managed, do not allow overgrowth of weeds or plants near the grapes.",
"4.Once the plants have been infected Remove all mummies from the canopy during the dormant pruning process. Mummies produce spores next to the susceptible grapevine tissues throughout the season; even relatively few can cause significant damage.” Another technique to rid of infection can be to “cultivate the vineyard before bud-break to bury the mummified berries. Diseased berries covered with soil do not produce spores that will reach the developing vines."]
},
{
'discription':"Grapevine measles, also called esca, black measles or Spanish measles, has long plagued grape growers with its cryptic expression of symptoms and, for a long time, a lack of identifiable causal organism(s).",
'name':"Grape___Esca_(Black_Measles)",
'remedy':["Presently, there are no effective management strategies for measles. Wine grape growers with small vineyards will often have field crews remove infected fruit prior to harvest. Raisins affected by measles will be discarded during harvest or at the packing house, while table grape growers will leave affected fruit on the vine. Current research is focused on protecting pruning wounds from fungal infections to minimize suspect fungi from colonizing fresh wounds."]
},
{'discription':"It's a healthy leaf",
'name':"Grape_healthy",
'remedy':["Maintain the plant"]},
{
    'discription':"The yellow-green disease spots gradually appear on the front of the grape leaves with downy mildew and white frosty mildew appears on the backs of the leaves",
    'name':"Grape___Leaf_blight",
    'remedy':["Spraying of the grapevines at 3-4 leaf stage with fungicides like Brodeaux mixture @ 0.8% or copper Oxychloride @ 0.25% are effective against this disease"],

},
{
'discription':"Citrus greening disease  is a disease of citrus caused by a vector-transmitted pathogen. The causative agents are motile bacteria, Liberibacter spp. The disease is vectored and transmitted by the Asian citrus psyllid, Diaphorina citri, and the African citrus psyllid, Trioza erytreae, also known as the two-spotted citrus psyllid",
'name':"Orange__Haunglongbing",
'remedy':["1.Advanced Nutritional Supplements -To slow the progression of citrus greening in infected trees, trace amounts of nutrients are applied to the leaves or to the roots",
"2.Reflective Mulch-reflective metalized polyethylene film used as mulch beneath newly planted citrus trees may impair the psyllids’ (insects which spread citrus greening) ability to find and infect citrus trees","3.Heat Treatment-Heating HLB-infected trees in the sun by encasing them in plastic “tents” slows or diminishes the psyllid count, which may potentially prolong the productivity of trees","4.Citrus Under Protective Screen (CUPS)-grow citrus that offer more protection from the psyllid. By growing citrus in an enclosed area, under screen, the citrus remains healthy and unaffected by citrus greening. More research is necessary to determine if this can be done on a large scale and whether costs could be reduced.","5.Biotechnologies-develop a disease-resistant breed of citrus tree which is not susceptible to greening or HLB and will not become diseased. As a result, the tree will remain healthy and continue to produce quality citrus fruit. This research includes traditional cross-breeding and biotechnology."]
},
{
'discription':"Bacterial spot is an important disease of peaches. Symptoms of this disease include fruit spots, leaf spots, and twig cankers. Fruit symptoms include pitting, cracking, gumming, and watersoaked tissue, which can make the fruit more susceptible to brown rot, rhizopus, and other fungal infections. Severe leaf spot infections can cause early defoliation. Severe defoliation can result in reduced fruit size, and sunburn and cracking of fruit. Early defoliated trees are reduced in vigor and winter hardiness.This peach tree leaf spot disease is caused by the bacterium Xanthomonas campestris pv. pruni. Bacterial spot on peach trees results in loss of fruit and the overall malaise of trees caused by recurrent defoliation. Also, these weakened trees are more susceptible to winter injury",
'name':"Peach___Bacterial_spot",
'remedy':["1.avoid low-lying or shaded sites with poor air circulation and soil drainage. Any practice that promotes faster drying of fruit and foliage will help reduce the risk of infection. Destroy nearby wild or neglected stone fruits","2.Prune trees annually to allow for better air circulation and to maintain tree vigor. If possible, prune during dry weather in the latter half of the dormant season",
"3.Fertilize where needed to maintain vigorous but not excessive shoot growth.","4.Select peach varieties with resistance to bacteria spot"]
},
{'discription':"It's a healthy leaf",
'name':"Peach_healthy",
'remedy':["Maintain the plant"]},
{
'discription':"Bacterial spot is one of the most devastating diseases of pepper and tomato. The disease occurs worldwide where pepper and tomato are grown in warm, moist areas. When it occurs soon after transplanting and weather conditions remain favorable for disease development, the results are usually total crop loss. Current chemical control is limited to copper or copper combined with maneb sprays that provide only marginal success thus making the disease very difficult to control once the epidemic is underway. When the disease occurs in commercial pepper fields early in the season, some farmers destroy the entire crop by disking because it is so difficult and economically costly to control once present in the field.",
'name':"Pepper,bell__Bacterial_spot",
'remedy':["1.In transplant production greenhouses, minimize overwatering and handling of seedlings when they are wet.",
"2.Trays, benches, tools, and greenhouse structures should be washed and sanitized between seedlings crops.",
"3.Crop rotation should be used to avoid pathogen carryover on volunteers and crop residue. Avoid fields that have been planted with peppers or tomatoes within one year, especially if they had bacterial spot previously.",
"4.Eliminate solanaceous weeds in and around tomato and pepper production areas.",
"5.Keep cull piles away from field operations.",
"6.Do not spray, tie, harvest, or handle wet plants as that can spread the disease."]
},
{'discription':"It's a healthy leaf",
'name':"Pepper,bell_healthy",
'remedy':["Maintain the plant"]},
{
'discription':"Early blight of potato is a common disease found in most potato growing regions. The disease is caused by the fungus Alternaria solani, which can also afflict tomatoes and other members of the potato family. Potatoes become infected with early blight when foliage has become excessively wet due to rain, fog, dew, or irrigation. Although not a terminal disease, severe infections can be fairly detrimental. In contrast to its name, early blight rarely develops early; it actually usually affects mature foliage rather than young, tender leaves.",
'name':"Potato___Early_blight",
'remedy':["1.Prune or stake plants to improve air circulation and reduce fungal problems.",
"2.Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut.",
"3.Keep the soil under plants clean and free of garden debris. Add a layer of organic compost to prevent the spores from splashing back up onto vegetation.",
"4.Drip irrigation and soaker hoses can be used to help keep the foliage dry."
"5.For best control, apply copper-based fungicides early, two weeks before disease normally appears or when weather forecasts predict a long period of wet weather. Alternatively, begin treatment when disease first appears, and repeat every 7-10 days for as long as needed."]
},
{'discription':"It's a healthy leaf",
'name':"Potato_healthy",
'remedy':["Maintain the plant"]},
{
'discription':"Late blight of potato is identified by blackish/brown lesions on leaves and stems that may be small at first and appear water-soaked or have chlorotic borders but expand rapidly and the entire leaf becomes become necrotic. In humid conditions, P. infestans produces sporangia and sporangiophores on the surface of infected tissue and the resulting white sporulation can be seen at the margins of lesions on abaxial (lower) surfaces of leaves (Figures 5). As many lesions accumulate, the entire plant can be destroyed in a matter of days after the first lesions are observed if the appropriate fungicide applications are not used .",
'name':"Potato___Late_blight",
'remedy':["1.Plant potatoes where no tomatoes, potatoes, peppers or eggplants have been for the past 3-4 years.",
"2.Keep leaves as dry as possible.",
"3.Remove or bury plants at the end of the season. Manage cull piles so culls break down over winter.",
"4.Control volunteer potato plants, as infected plants can grow from infected tubers.",
"5.Seed infection is unlikely on commercially prepared tomato seed or on saved seed that has been thoroughly dried."]
},
{
'discription':"Powdery mildew infections are caused by several different species of fungus. Each species has its own preferred host plants. The species of powdery mildew that affects squash foliage (Erysiphe cichoracearum) is different from those that target peas (Erysiphe pisi) or eggplants (Leveillula taurica). Interestingly, this fungus lives on the outside of the leaves and does not penetrate the interior tissue. It can only grow on the surface of the leaf.Regardless of which plant is being attacked by which species, the appearance of powdery mildew is the same. It is one of the most common plant diseases, and because its appearance is so distinct, it’s fairly easy to identify. Powdery mildew  makes the leaves look like they’ve been dusted with talcum powder. The mildew is white to gray. Most of that white dust consists of spores which are easily carried by wind to other nearby leaves.",
'name':"Squash___Powdery_mildew",
'remedy':["1.Baking soda solution: Mix 1 tablespoon baking soda and ½ teaspoon liquid soap such as Castile soap (not detergent) in 1 gallon of water. Spray liberally, getting top and bottom leaf surfaces and any affected areas. This method may work better as a preventative measure, although it does have some effect on existing powdery mildew as well.",
"2.Potassium bicarbonate: Mix 1 tablespoon potassium bicarbonate and ½ teaspoon liquid soap (not detergent) in 1 gallon of water. Spray liberally to all affected areas. This mixture may work better than baking soda as a treatment for existing infections.",
"3.Milk: Mix 1 part milk to 2 to 3 parts water and spray liberally. While the science behind this solution isn’t fully understood, it seems to work rather well, especially on zucchini, melons and cucumbers. It is believed that naturally-occurring compounds in the milk not only combat the disease, but also boost the plant’s immune system.",
"4.Neem oil: By itself, neem oil has mixed reviews on its effectiveness to treat powdery mildew, but it can be added to the above mixtures for an extra boost.",
"5.Powdery mildew fungicide: Use sulfur-containing organic fungicides as both preventive and treatment for existing infections."]
},
{'discription':"It's a healthy leaf",
'name':"Strawberry_healthy",
'remedy':["Maintain the plant"]},
{
'discription':"Scorched strawberry leaves are caused by a fungal infection which affects the foliage of strawberry plantings. The fungus responsible is called Diplocarpon earliana. Strawberries with leaf scorch may first show signs of issue with the development of small purplish blemishes that occur on the topside of leaves.",
'name':"Strawberry leaf scorch",
'remedy':["1.Since this fungal pathogen overwinters on the fallen leaves of infected plants, proper garden sanitation is key. This includes the removal of infected garden debris from the strawberry patch, as well as the frequent establishment of new strawberry transplants."
"2.When making new plantings always ensure that good planting practices are implemented. These practices include the use of proper plant spacing to provide adequate air circulation and the use of drip irrigation."]
},
{
'discription':"Bacterial spot is among the most devastating tomato diseases due to its ability to spread quickly and its resistance to control methods. Caused by four species of Xanthomonas, bacterial spot occurs all over the world wherever tomatoes are cultivated.",
'name':"Tomato Bacterial spot",
'remedy':["1.One of the best ways to avoid bringing bacterial spot into the garden is to purchase certified disease-free tomato seeds." 
"2.Gardeners should always use either a sterilized soil medium or one that is commercially made."
"3.Practicing crop rotation will help lessen the spread of bacterial spot. Because moist conditions and humidity attract bacterial spot, watering should be done in the early morning hours to allow plants plenty of time to dry out before the afternoon heat comes along."]
},
{
'discription':"Common on tomato and potato plants, early blight is caused by the fungus Alternaria solani . Symptoms first appear on the lower, older leaves as small brown spots with concentric rings that form a “bull’s eye” pattern. As the disease matures, it spreads outward on the leaf surface causing it to turn yellow, wither and die. Eventually the stem, fruit and upper portion of the plant will become infected. Crops can be severely damaged.",
'name':"Tomato Early blight",
'remedy':["1.Thoroughly spray the plant (bottoms of leaves also) with Bonide Liquid Copper Fungicide concentrate or Bonide Tomato & Vegetable."
"2.Make sure to disinfect your pruning shears (one part bleach to 4 parts water) after each cut."
"3.Drip irrigation and soaker hoses can be used to help keep the foliage dry."]
},
{'discription':"It's a healthy leaf",
'name':"Tomato_healthy",
'remedy':["Maintain the plant"]},
{
'discription':"Late blight first appears on the lower, older leaves as water-soaked, gray-green spots. As the disease matures, these spots darken and a white fungal growth forms on the undersides. Eventually the entire plant will become infected. ",
'name':"Tomato Late blight",
'remedy':["1.Plant resistant cultivars when available",
"2.Remove volunteers from the garden prior to planting and space plants far enough apart to allow for plenty of air circulation.",
"3.Water in the early morning hours, or use soaker hoses, to give plants time to dry out during the day — avoid overhead irrigation."]
},
{
'discription':"Leaf mold of tomato is caused by pathogen Passalora fulva. It is found throughout the world, predominantly on tomatoes grown where the relative humidity is high, particularly in plastic greenhouses.",
'name':"Tomato Leaf Mold",
'remedy':["1.When planting, use only certified disease-free seed or treated seed.",
"2.Remove and destroy all crop debris post-harvest.",
"3.Use fans and avoid overhead watering to minimize leaf wetness."]
},
{
'discription':"Septoria leaf spot is a very common disease of tomatoes.1﻿ It is caused by a fungus (Septoria lycopersici) and can affect tomatoes and other plants in the Solanaceae family, especially potatoes and eggplant, just about anywhere in the world.",
'name':"Tomato septoria leaf spot",
'remedy':["1.Removing infected leaves. Remove infected leaves immediately, and be sure to wash your hands and pruners thoroughly before working with uninfected plants.",
"2.Consider organic fungicide options",
"3.Consider chemical fungicides."]
},
{
'discription':"As the summer heat continues, it is common to see spider mites on commercial and home-grown tomatoes. Heat, drought, water stress, the presence of a large number of weeds, and incorrect use of insecticides can lead to high buildup of mites on tomatoes .The two-spotted spider mite is a common species on tomatoes in the south and is distinguishable by a pair of dark spots visible through the orange body. The dark spots on spider mites are generally the accumulation of body waste under the skin, hence the newly formed individuals may lack the spots.",
'name':"Tomato___Spider_mites Two-spotted_spider_mite",
'remedy':["1.Abamectin is actually a naturally derived substance and serves as a good rescue insecticide. AgriMek contains synthetic abamectin and provides long-term residual control of two-spotted spider mites",
"2.This is a contact poison against two-spotted spider mites with less toxicity to predaceous mites and beneficial arthropods."
 "3.Zeal is a growth regulator specific to plant-feeding mites, and it doesn’t harm mite predators. Zeal has translaminar activity like abamectin and kills eggs and nymphs of the two-spotted spider mites plus it sterlizes the adults."]
},
{
'discription':"Target spot of tomato is caused by the fungal pathogen Corynespora cassiicola.1 The disease occurs on field-grown tomatoes in tropical and subtropical regions of the world. ",
'name':"tomato target spot ",
'remedy':["1.Warm wet conditions favour the disease such that fungicides are needed to give adequate control. The products to use are chlorothalonil, copper oxychloride or mancozeb."
"2.After harvest:Collect and burn as much of the crop as possible when the harvest is complete.Practise crop rotation, leaving 3 years before replanting tomato on the same land."]
},
{
'discription':"Tomato mosaic virus is a serious and extremely contagious disease. It is also hard to identify, with symptoms varying wildly depending upon the variety and age of the infected plant, the strain of the virus, and environmental conditions. To make matters worse, it is very hard to distinguish from the closely related tobacco mosaic virus.",
'name':"Tomato___Tomato_mosaic_virus",
'remedy':["1.Remove all infected plants and destroy them. Do NOT put them in the compost pile, as the virus may persist in infected plant matter. ",
"2.Monitor the rest of your plants closely, especially those that were located near infected plants.",
"3.Disinfect gardening tools after every use."]
},
{
'discription':"TYLCV is transmitted by adult silverleaf whiteflies and can spread rapidly, but TYLCV is not transmitted through seed or by mechanical transmission. The presence of silverleaf whitefly host plants, both cultivated (peppers and tomatoes) or wild hosts (sowthistle, cheeseweed and nightshade weeds) during spring and summer may lead to whitefly migration and spread of TYLCV. ",
'name':"Tomato___Tomato_Yellow_Leaf_Curl_Virus",
'remedy':["1.Use a neonicotinoid insecticide, such as dinotefuran (Venom) imidacloprid (AdmirePro, Alias, Nuprid, Widow, and others) or thiamethoxam (Platinum), as a soil application or through the drip irrigation system at transplanting of tomatoes or peppers."
"2.Sanitation is very important for preventing the migration of whitefly adults and the spread of TYLCV. Rogue tomato or pepper plants with early symptoms of TYLCV can be removed from fields by placing infected-looking plants in plastic bags immediately at the beginning season, especially during first three to four weeks." ]
},
]}
    return jsonify(person)
    


if __name__ == '__main__':
    app.run()

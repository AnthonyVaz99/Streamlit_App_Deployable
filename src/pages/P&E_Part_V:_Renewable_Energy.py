import json
import streamlit as st
from streamlit_lottie import st_lottie

# Creating sidebar message to prompting user to choose a directory 
st.sidebar.success("Choose a page from directory above.")

# Function to load Lottie File animations
def load_lottie_file(filepath: str):
    with open(filepath, 'r') as f:
        return json.load(f)

# Linking all of the pages at the top of the page
st.page_link('Main_Page.py', label="Home Page")
st.page_link('pages/Emissions_By_Decade.py', label="Page 1: Emissions by Decade")
st.page_link('pages/P&E_Part_I:_What_IS_Pollution.py', label="Page 2: P&E 1 - What is Pollution")
st.page_link('pages/P&E_Part_II:_Three_Major_Types_Pollution.py', label="Page 3: P&E 2 - Three Types of Pollution")
st.page_link('pages/P&E_Part_III:_What_IS_Energy.py', label="Page 4: P&E 3 - What is Energy")
st.page_link('pages/P&E_Part_IV:_Energy_Creation,_Storage,_&_Transfer.py', label="Page 5: P&E 4 - Energy Creation, Storage & Transfer")
st.page_link('pages/P&E_Part_V:_Renewable_Energy.py', label="Page 6: P&E 5 - Renewable Energy")

# Page title and subtitle, with spacing and dividers
st.header(' ',divider='grey')
st.title(":blue[Pollution and Energy Overview V]")
st.header(' ',divider='grey')
st.write(' ')
st.write(' ')
st.write(' ')
st.write(':grey[Part V:] :orange[Renewable Energy: The Future We Need]')
st_lottie(load_lottie_file('src/animations/transition.json'))
if st.checkbox(":grey[Click to view video on renewable energy 101.]"):
    st.video(data='https://youtu.be/T4xKThjcKaE?si=EIsytgYBaSZJW3uL')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.subheader(' ', divider='grey')

st.header(':orange[Solar Power]')
st.write(':orange[Solar power], also known as solar :orange[energy], is the :green[renewable energy] derived from the :orange[suns radiation]. It is harnessed using mainly solar panels, but also various technologies to generate :orange[electricity], :orange[heat], or :orange[light] for various applications. :orange[Solar power] is abundant, sustainable, and environmentally friendly, making it a key focus in the :orange[transition] towards cleaner :orange[energy sources].')
st_lottie(load_lottie_file('src/animations/solar.json'))
st.header(':orange[Types of Solar Power Systems]')
st.write(':orange[Solar Photovoltaic(PV)] technology converts :orange[sunlight] directly into :orange[electricity] using :orange[photovoltaic cells], typically made of :orange[silicon] or other :orange[semiconductor] materials. When :orange[sunlight] hits these cells, it generates an :orange[electric] current through the :orange[photovoltaic] effect.')
st.write(':orange[Concentrated Solar Power(CSP)] systems use mirrors or lenses to :orange[concentrate sunlight] onto a receiver, where the concentrated :orange[heat] is used to produce :orange[steam] and drive :orange[turbines] to generate :orange[electricity.]')
st.write(':orange[Passive solar] heating techniques utilize :orange[building design] and materials to capture and store :orange[solar heat] for space :orange[heating] and :orange[cooling]. Strategies include :orange[orientation], :orange[insulation], :orange[thermal mass:orange], and :orange[shading] to optimize solar gain and minimize heat loss.')
if st.checkbox('Click to view video on solar power.'):
    st.video(data='https://youtu.be/yFwGpiCs3ss?si=eJe0_jeyXCUGU5oi')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :orange[solar power:orange[ offers significant potential for :green[clean], :green[sustainable energy generation] and plays a crucial role in :orange[reducing greenhouse gas emissions], :orange[diversifying energy sources], and :orange[promoting energy security] and :orange[resilience]. Continued technological advancements and policy support are essential to further enhance the deployment and integration of solar power into the global energy mix.')
st.subheader(' ', divider='grey')

st.header(':blue[Wind Power]')
st.write(':blue[Wind power] is a :green[renewable energy] resource generated by harnessing the :blue[kinetic energy] of :blue[wind] to produce :blue[electricity]. It is one of the fastest-growing sources of :green[clean energy] worldwide and has become a key component of efforts to transition to a :blue[low-carbon economy].')
st_lottie(load_lottie_file('src/animations/windpower.json'))
st.header(':blue[Types of Wind Power Systems]')
st.write(':blue[Wind power] is generated using :blue[wind turbines], which are tall structures with rotor blades mounted on a hub. The rotating blades :blue[capture the kinetic energy] of the wind and convert it into :blue[mechanical energy]. The :blue[mechanical energy] is then converted into :blue[electricity] by a :blue[generator] housed inside the turbines :blue[nacelle](the housing on top of the tower). The generator produces :blue[alternating current(AC) electricity], which is typically transmitted to the :blue[electrical grid] for distribution.')
st.write(':blue[Wind turbines] are often grouped together in :blue[wind farms], where multiple :blue[turbines] are installed in close proximity to :blue[maximize energy production]. :blue[Wind farms] can range in size from small, community-owned installations to large-scale utility projects with hundreds of turbines covering vast areas of land or offshore sites.')
st.write(':blue[Onshore wind] farms are located on land, typically in open areas with :blue[strong and consistent wind speeds]. They are more common and less expensive to develop compared to :blue[offshore wind farms]. :blue[Offshore wind farms] are located in :blue[bodies of water], such as :blue[oceans] or :blue[lakes], where wind speeds tend to be :blue[higher and more consistent]. :blue[Offshore wind farms] can be located relatively close to shore(:blue[nearshore]) or further away from shore(:blue[offshore]).')
if st.checkbox('Click to view video on wind power.'):
    st.video(data='https://youtu.be/Z5c50-_hcD0?si=9iwC_cI8glXEZrGa')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :blue[wind power] offers significant potential for :green[clean], :green[sustainable energy generation] and plays a vital role in :blue[reducing greenhouse gas emissions], :blue[combating climate change], and :blue[achieving global energy transition goals]. Continued technological innovation, policy support, and community engagement are essential to further enhance the deployment and integration of :blue[wind power] into the energy mix.')
st.subheader(' ', divider='grey')

st.header(':blue[Hydropower]')
st.write(':blue[Hydropower], also known as :blue[hydroelectric power], is a :green[renewable energy] resource generated by harnessing the :blue[energy] of :blue[flowing water] to produce :blue[electricity]. It is one of the oldest and most widely used forms of :green[renewable energy], with :blue[hydroelectric power plants] operating around the world.')
st_lottie(load_lottie_file('src/animations/hydro.json'))
st.header(':blue[Types of  Hydroower Systems]')
st.write(':blue[Hydropower] is generated by :blue[hydroelectric power plants], which use :blue[turbines] and :blue[generators] to :blue[convert the kinetic energy of flowing water into electricity]. These power plants are typically located near :blue[rivers], :blue[streams], or other :blue[water sources:blue with sufficient flow and elevation difference] to generate power :blue[efficiently].')
st.write(':blue[Reservoir Hydropower]: These systems use :blue[dams] to create :blue[reservoirs], storing water during periods of low demand and :blue[releasing it through turbines to generate electricity] during peak demand.')
st.write(':blue[Run-of-River Hydropower]: In run-of-river systems, :blue[water flows naturally] downstream without significant storage or regulation. :blue[Turbines] are installed directly in the :blue[river] or :blue[stream] to capture :blue[kinetic energy] from the :blue[flowing water].')
st.write(':blue[Pumped Storage Hydropower]: Pumped storage facilities :blue[store excess electricity] by :blue[pumping water from a lower reservoir to an upper reservoir during periods of low demand]. When :blue[electricity] demand :blue[increases], :blue[water is released from the upper reservoir] to :blue[generate electricity] through :blue[turbines].')
if st.checkbox('Click to view video on hydropower.'):
    st.video(data='https://youtu.be/q8HmRLCgDAI?si=oT1fQ984_OQFoLAs')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :blue[hydropower] offers significant potential for :green[clean, renewable energy generation] and plays a crucial role in :blue[reducing greenhouse gas emissions], :blue[enhancing energy security], and :blue[promoting sustainable development]. Continued innovation, environmental stewardship, and stakeholder engagement are essential to maximize the benefits of :blue[hydropower] while addressing its challenges and impacts.')
st.subheader(' ', divider='grey')

st.header(':blue[Tidal Power]')
st.write(':blue[Tidal power], also known as :blue[tidal energy], is a :green[renewable energy] resource generated by harnessing the energy of :blue[tidal currents] and :blue[ocean tides] to :blue[produce electricity]. It is a form of :blue[hydropower] that utilizes the gravitational forces of the moon and the sun, which cause the rise and fall of ocean tides. ')
st_lottie(load_lottie_file('src/animations/tidal.json'))
st.header(':blue[Types of Tidal Power Systems]')
st.write(':blue[Tidal power] is generated using :blue[tidal turbines], similar to wind turbines but designed to operate underwater. These turbines are placed in :blue[tidal streams] or near coastal areas :blue[where tidal currents are strong]. As tidal currents flow, they drive the rotors of the :blue[turbines], which are connected to :blue[generators that produce electricity]. The rotational energy of the turbines is converted into electrical energy through electromagnetic induction.')
st.write(':blue[Tidal Stream Systems]: Tidal stream systems utilize :blue[underwater turbines] placed in :blue[tidal currents] to capture :blue[kinetic energy from moving water]. These systems can be deployed in arrays to :blue[maximize energy production] and are often installed on the seabed or anchored to fixed structures.')
st.write(':blue[Tidal Barrages]: Tidal barrages are large dams or barriers built across estuaries or tidal basins to :blue[capture and store water during high tides]. When the tide :blue[recedes], :blue[water is released through turbines to generate electricity]. Tidal barrages can provide a reliable and predictable source of energy but may have significant environmental and social impacts.')
if st.checkbox('Click to view video on tidal power.'):
    st.video(data='https://youtu.be/VkTRcTyDSyk?si=Ct1oHWw46bfjm6m-')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :blue[tidal power] offers significant potential as a :green[clean, renewable energy] source, particularly in regions with suitable :blue[tidal resources]. Continued technological innovation, environmental research, and policy support are essential to overcome challenges and unlock the full benefits of tidal energy for sustainable energy production.')
st.subheader(' ', divider='grey')

st.header(':green[Geothermal Power]')
st.write(':green[Geothermal power] is a :green[renewable energy] resource derived from the :green[heat stored beneath the Earths surface]. It harnesses the :green[natural heat energy from the Earths interior to generate electricity] and provide :green[heating] and :green[cooling] for various applications.')
st_lottie(load_lottie_file('src/animations/geothermal.json'))
st.header(':green[Types of Geothermal Power Systems]')
st.write(':green[Geothermal energy] originates from the heat stored :green[within the Earths crust], primarily from :green[radioactive decay of minerals] and :green[heat leftover from the planets formation]. Heat from the Earths interior is :green[transferred] to the surface through :green[conduction], :green[convection], and :green[volcanic activity], creating :green[geothermal reservoirs] of hot water and steam.')
st.write(':green[Geothermal energy] is also used for :green[direct heating and cooling] applications, such as :green[district heating systems], :green[space heating], and :green[greenhouse heating]. :green[Geothermal heat pumps](also known as :green[ground-source heat pump]s) use the relatively stable temperature of the ground to provide efficient heating and cooling for buildings. They :green[circulate a fluid] through underground pipes to :green[absorb heat from the ground] during winte(heating mode) :green[or dissipate heat into the ground] during summer(cooling mode).')
if st.checkbox('Click to view video on geothermal power.'):
    st.video(data='https://youtu.be/DFQrE91kZwk?si=gP-sWp8v8B4cUXwO')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :green[geothermal power] offers significant potential as a :green[clean], :green[reliable], and :green[versatile energy source] for electricity generation, heating, and cooling. Continued technological advancements, resource assessment, and policy support are essential to unlock the full benefits of geothermal energy and promote its widespread adoption as part of the global energy transition.')
st.subheader(' ', divider='grey')

st.header(':green[Biomasss Power]')
st.write(':green[Biomass power] is a :green[renewable energy] resource derived from :green[organic materials] such as :green[plant matter], :green[agricultural residues], :green[wood waste], and :green[organic waste] from industries, households, and municipal sources. It involves :green[converting] the :green[chemical energy] stored in :green[biomass] into :green[heat], :green[electricity], or :green[biofuels] through various processes, and some processes that :green[create energy from biomass are:]')
st_lottie(load_lottie_file('src/animations/biomass.json'))
st.header(':green[Types of Biomass Power Systems]')
st.write(':green[Biomass Combustion]: Biomass combustion involves :green[burning organic materials] in boilers or furnaces to produce heat energy. The heat can be used directly for :green[space heating], :green[water heating], or :green[industrial processes], or it can be used to generate steam to drive turbines and :green[produce electricity in biomass power plants].')
st.write(':green[Biomass Gasification]: Biomass gasification :green[converts solid biomass] into a :green[gaseous fuel] through partial oxidation in a high-temperature, oxygen-limited environment. The gaseuous fuel can be used for :green[electricity generation], :green[heating], or as a :green[feedstock for biofuels production].')
st.write(':green[Anaerobic Biomass Digestion]: Anaerobic digestion is a biological process that :green[breaks down organic materials] in the :green[absence of oxygen], :green[producing biogas:green[(a mixture of methane and carbon dioxide) and :green[digestate]. :green[Biogas] can be used directly as a :green[fuel for heating or electricity generation], or it can be :green[upgraded to biomethane] for injection into natural gas pipelines or use as a transportation fuel.')
st.write(':green[Biochemical Biomass Conversion]: Biochemical conversion processes, such as :green[fermentation], :green[hydrolysis], and :green[enzymatic digestion], break down biomass feedstocks into :green[sugars], :green[alcohols], and other :green[organic compound]s. These compounds can be used to :green[produce biofuels] such as :green[bioethanol], :green[biodiesel], and :green[biobutanol].')
if st.checkbox('Click to view video on biomass power.'):
    st.video(data='https://youtu.be/yHWcddUZ35s?si=3TXKyatXmuPBHoH9')
    st.write(':grey[Video from Student Energy on YouTube.]')
st.write('Overall, :green[biomass] power offers significant potential as a :green[versatile], :green[renewable energy source] for :green[electricity generation], :green[heating], and :green[transportation fuels]. Continued technological innovation, policy support, and sustainable management practices are essential to maximize the benefits of biomass energy and mitigate its challenges and environmental impacts.')
st.subheader(' ', divider='grey')

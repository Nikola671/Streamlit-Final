# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 08:10:25 2024

@author: nikol
"""

import streamlit as st
from streamlit_folium import folium_static
import folium
import requests

st.title("U.S. Colloquialisms")
st.caption("This map of the United States displays some unique words or phrases residents use in each state.")
st.caption("Refer to the Magical Sidebar to position map if needed.")

usmap = folium.Map(location=[39.8283, -95], zoom_start=4)

us_states = requests.get(
    "https://raw.githubusercontent.com/python-visualization/folium-example-data/main/us_states.json"
).json()

colloquialisms = {
    "Alabama": "Roll Tide! - A cheer for the University of Alabama's football team, the Crimson Tide.",
    "Alaska": "Bush pilot - A pilot who flies small aircraft into remote areas.",
    "Arizona": "Haboob - A type of intense dust storm common in the desert regions.",
    "Arkansas": "Woo pig sooie! - A cheer for the University of Arkansas Razorbacks.",
    "California": "Hella - A slang term meaning 'very' or 'a lot.'",
    "Colorado": "Fourteener - A mountain peak exceeding 14,000 feet in elevation.",
    "Connecticut": "Borough - A term used to refer to a town or village within a larger city.",
    "Delaware": "Slower Lower - Referring to the southern part of Delaware, known for its relaxed pace of life.",
    "Florida": "Snowbird - A term for seasonal residents, typically retirees, who migrate to Florida during the winter months.",
    "Georgia": "Hotlanta - A nickname for Atlanta, referencing its hot and humid climate.",
    "Hawaii": "Pau hana - A Hawaiian term meaning 'after work,' often used to refer to happy hour or leisure time.",
    "Idaho": "Spud - A slang term for a potato, referencing Idaho's status as a major potato-producing state.",
    "Illinois": "Chi-town - A nickname for Chicago.",
    "Indiana": "Hoosier - A term for a resident of Indiana, but its origin is uncertain.",
    "Iowa": "Iowan nice - Refers to the friendliness and hospitality often associated with people from Iowa.",
    "Kansas": "Sunflower State - A nickname for Kansas, known for its fields of sunflowers.",
    "Kentucky": "Bluegrass State - A nickname for Kentucky, referring to the bluegrass found in many of its pastures.",
    "Louisiana": "Lagniappe - A Cajun term meaning 'a little something extra.'",
    "Maine": "Wicked - An intensifier often used in Maine, meaning 'very' or 'extremely.'",
    "Maryland": "Hon - A term of endearment often used in Baltimore.",
    "Massachusetts": "Pahk the cah in Hahvahd Yahd - A Bostonian accent phrase meaning 'park the car in Harvard Yard.'",
    "Michigan": "Yooper - A term for residents of Michigan's Upper Peninsula.",
    "Minnesota": "Uff da - An expression of surprise, amazement, or exhaustion commonly used in Minnesota.",
    "Mississippi": "Mudcat - A term for a catfish found in muddy waters, commonly caught in the Mississippi River.",
    "Missouri": "Show-Me State - A nickname for Missouri, reflecting the state's residents' skeptical nature.",
    "Montana": "Big Sky Country - A nickname for Montana, referencing its expansive skies and wide-open spaces.",
    "Nebraska": "Husker - A term for a fan or supporter of the University of Nebraska Cornhuskers.",
    "Nevada": "Silver State - A nickname for Nevada, referencing its history of silver mining.",
    "New Hampshire": "Granite State - A nickname for New Hampshire, referring to its abundant granite quarries.",
    "New Jersey": "Jersey Devil - A mythical creature said to inhabit the Pine Barrens of New Jersey.",
    "New Mexico": "Land of Enchantment - A nickname for New Mexico, reflecting its scenic beauty and cultural heritage.",
    "New York": "The Big Apple - A nickname for New York City.",
    "North Carolina": "Tar Heel - A term for a resident of North Carolina, with uncertain origins.",
    "North Dakota": "Roughrider State - A nickname for North Dakota, honoring the state's history of the Rough Riders, a volunteer cavalry unit.",
    "Ohio": "Buckeye - A term for a resident of Ohio, as well as the state tree and state nickname.",
    "Oklahoma": "Sooner - A term for a resident of Oklahoma, as well as the University of Oklahoma mascot.",
    "Oregon": "Beaver State - A nickname for Oregon, referencing the state animal.",
    "Pennsylvania": "Yinz - A Pittsburgh dialect term for 'you all' or 'you guys.'",
    "Rhode Island": "Quahog - A type of clam commonly found in Rhode Island, also the name of the fictional town in 'Family Guy.'",
    "South Carolina": "Palmetto State - A nickname for South Carolina, referencing the state tree.",
    "South Dakota": "Mount Rushmore State - A nickname for South Dakota, referring to the famous monument.",
    "Tennessee": "Volunteer State - A nickname for Tennessee, reflecting its history of volunteerism.",
    "Texas": "Y'all - A contraction of 'you all,' commonly used in Texas and the Southern United States.",
    "Utah": "Beehive State - A nickname for Utah, referencing the state's emblem and industriousness.",
    "Vermont": "Green Mountain State - A nickname for Vermont, referring to the Green Mountains that traverse the state.",
    "Virginia": "Old Dominion - A nickname for Virginia, reflecting its status as one of the original Thirteen Colonies.",
    "Washington": "Evergreen State - A nickname for Washington, referencing its abundant evergreen forests.",
    "West Virginia": "Mountain State - A nickname for West Virginia, reflecting its mountainous terrain.",
    "Wisconsin": "Cheesehead - A term for a resident of Wisconsin, as well as a colloquial term for a fan of the Green Bay Packers.",
    "Wyoming": "Cowboy State - A nickname for Wyoming, reflecting its cowboy and ranching heritage."
}

with st.sidebar:
    st.header("Magical Sidebar")
    if st.button("Continental U.S."):
        usmap.location = [39.8283, -95]
        usmap.zoom_start = 4
    if st.button("Alaska"):
        usmap.location = [63.59, -154.49]
        usmap.zoom_start = 3.5
    if st.button("Hawaii"):
        usmap.location = [19.90, -155.67]
        usmap.zoom_start = 5.5



#The top half of code above is to create the map and data for the states on the map, the code
#below is to create the popup for each state. This bottom half of the code is what has been
#not working as intended. When running on streamlit, the map works with no problems, 
#however the popups do not appear. If you are able to discover the issue and how to 
#resolve it I would be greately appreciatvie.






def popup_content(feature):
    state_name = feature['properties']['name']
    colloq = colloquialisms.get(state_name, "Placeholder")
    popup_text = f"<b>State:</b> {state_name}<br><i>Unique phrase:</i> {colloq}"
    return folium.Popup(popup_text, max_width=300
          )              
                        
folium.GeoJson(
    us_states,
    style_function = lambda feature: {
        'fillColor': 'purple',
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.45
    },
    popup = popup_content,
    highlight_function = lambda feature: {
        'weight': 3,
        'color': '#666',
        'fillOpacity': 0.7,
    },
).add_to(usmap)

folium_static(usmap)










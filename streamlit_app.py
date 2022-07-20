import folium
import streamlit as st
from streamlit_folium import st_folium


def draw_folium_map():
    center = [39.5, -98.5]
    tiles = ["cartodbpositron", "Stamen Toner", "OpenStreetMap"]
    map = folium.Map(
        location=[center[0], center[1]],
        zoom_start=10,
        zoom_control=True,
        scrollWheelZoom=False,
        tiles=tiles[0],
    )
    folium.Marker(
        location=[39.5, -98.5],
        popup=f"A location!",
        icon=folium.Icon(color="blue", icon="star"),
    ).add_to(map)

    return map


def main():
    map_placeholder = st.empty()

    col1, col2, col3 = st.columns(3)
    # check1 = col1.checkbox("check1", True)

    col4, col5, col6 = st.columns(3)
    # check1 = col4.checkbox("check2", True)

    map = draw_folium_map()
    with map_placeholder.container():
        output = st_folium(map, width=700, height=450, key="foliumMap1")

    st.write(output)


if __name__ == "__main__":
    main()

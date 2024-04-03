async function initMap() {
  const lucernePosition = { lat: 45.50713348388672, lng: -73.66159057617188 };
  const jeanTalonPosition = { lat: 45.501077, lng: -73.646349 };

  //@ts-ignore
  const { Map } = await google.maps.importLibrary("maps");
  const { Marker } = await google.maps.importLibrary("marker");

  const styledMapType = new google.maps.StyledMapType(
    [
      {
        "featureType": "water",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#d3d3d3"
          }
        ]
      },
      {
        "featureType": "transit",
        "stylers": [
          {
            "color": "#808080"
          },
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "visibility": "on"
          },
          {
            "color": "#b3b3b3"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "visibility": "on"
          },
          {
            "color": "#ffffff"
          },
          {
            "weight": 1.8
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#d7d7d7"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "visibility": "on"
          },
          {
            "color": "#ebebeb"
          }
        ]
      },
      {
        "featureType": "administrative",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#a7a7a7"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "landscape",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "visibility": "on"
          },
          {
            "color": "#efefef"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#696969"
          }
        ]
      },
      {
        "featureType": "administrative",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "visibility": "on"
          },
          {
            "color": "#737373"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels.icon",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "geometry.stroke",
        "stylers": [
          {
            "color": "#d6d6d6"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "labels.icon",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {},
      {
        "featureType": "poi",
        "elementType": "geometry.fill",
        "stylers": [
          {
            "color": "#dadada"
          }
        ]
      }
    ],
    { name: "Map" },
  );

  map = new Map(document.getElementById("map"), {
    zoom: 13,
    center: lucernePosition,
    mapId: "524c2714b675479", // Change this to your map ID
    mapTypeControlOptions: {
      mapTypeIds: ["styled_map"],
    },
  });

  map.mapTypes.set("styled_map", styledMapType);
  map.setMapTypeId("styled_map");

  
  // Template for new location marker

  // const locationMarker = new Marker({ // Change location to desired place
  //   map: map,
  //   position: locationPosition, // Change location to desired place
  //   icon: "../images/map-marker.png",
  //   title: "Location", // Change location to desired place
  // });

  const lucerneMarker = new Marker({
    map: map,
    position: lucernePosition,
    icon: "../images/map-marker.png",
    title: "Lucerne",
  });

  const jeanTalonMarker = new Marker({
    map: map,
    position: jeanTalonPosition,
    icon: "../images/map-marker.png",
    title: "JeanTalon",
  });

  let store_info = document.querySelector(".google-map__marker-detail");

  // Template for new location store selector

  // let store_selector_Location = document.querySelector("#store_selector_Location"); // Change store_selector_Location to Desired place "Twice"
  // if (store_selector_Location) { // Change store_selector_Location to Desired place
  //   store_selector_Location.addEventListener("click", function (e) { // Change store_selector_Location to Desired place
  //     store_info.classList.remove("hide");
  //     map.setCenter(locationMarker.getPosition()); // Change locationMarker to Desired place
  //     map.setZoom(17);
  //     document.querySelector(".google-map__marker-detail__content").innerHTML =
  //       store_selector_Location.closest(".store-location__search-result__item").innerHTML; // Change store_selector_Location to Desired place
  //   }, false);
  // }

  let store_selector_Lucerne = document.querySelector("#store_selector_Lucerne");
  if (store_selector_Lucerne) {
    store_selector_Lucerne.addEventListener("click", function (e) {
      store_info.classList.remove("hide");
      map.setCenter(lucerneMarker.getPosition());
      map.setZoom(17);
      document.querySelector(".google-map__marker-detail__content").innerHTML =
        store_selector_Lucerne.closest(".store-location__search-result__item").innerHTML;
    }, false);
  }

  let store_selector_Jean_Talon = document.querySelector("#store_selector_Jean_Talon");
  if (store_selector_Jean_Talon) {
    store_selector_Jean_Talon.addEventListener("click", function (e) {
      store_info.classList.remove("hide");
      map.setCenter(jeanTalonMarker.getPosition());
      map.setZoom(17);
      document.querySelector(".google-map__marker-detail__content").innerHTML =
        store_selector_Jean_Talon.closest(".store-location__search-result__item").innerHTML;
    }, false);
  }

  let store_info_close_btn = document.querySelector(".google-map__marker-detail .btn-close");
  if (store_info_close_btn && store_info) {
    store_info_close_btn.addEventListener("click", function (e) {
      store_info.classList.add("hide");
    }, false);
  }
}


initMap();
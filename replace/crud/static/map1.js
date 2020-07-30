var guigui = new naver.maps.LatLng(37.603641, 127.043013),
    map = new naver.maps.Map('map1', {
        center: guigui.destinationPoint(0, 500),
        zoom: 20
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: guigui
    });

var contentString = [
        '<div class="iw_inner">',
        '   <h3>육가구이구이</h3>',
        '   <p> 서울특별시 성북구 월곡2동 장월로1길 <br/>',
        '   </p>',
        '</div>'
    ].join('');

var infowindow = new naver.maps.InfoWindow({
    content: contentString
});

naver.maps.Event.addListener(marker, "click", function(e) {
    if (infowindow.getMap()) {
        infowindow.close();
    } else {
        infowindow.open(map, marker);
    }
});

infowindow.open(map, marker);

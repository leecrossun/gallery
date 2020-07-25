var sabor = new naver.maps.LatLng(37.603682, 127.042842),
    map = new naver.maps.Map('map2', {
        center: sabor.destinationPoint(0, 500),
        zoom: 20
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: sabor
    });

var contentString = [
        '<div class="iw_inner">',
        '   <h3>사보르 김밥전문점</h3>',
        '   <p> 서울특별시 성북구 하월곡동 17-7 <br/>',
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

var sam = new naver.maps.LatLng(37.605548, 127.045036),
    map = new naver.maps.Map('map3', {
        center: sam.destinationPoint(0, 500),
        zoom: 20
    }),
    marker = new naver.maps.Marker({
        map: map,
        position: sam
    });

var contentString = [
        '<div class="iw_inner">',
        '   <h3>카페 샘</h3>',
        '   <p> KR 서울특별시 성북구 상월곡동 57-23번지 1층 1호 필지 <br/>',
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

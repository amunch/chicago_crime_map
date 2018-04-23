import csv

if __name__ == "__main__":
    filename = "hm.html"
    with open(filename,"w+") as f:
        firstpart = "<!DOCTYPE html><html><head><meta charset=\"utf-8\"><title>Heatmaps</title><style>#map {height: 100%;}html, body {height: 100%;margin: 0;padding: 0;}#floating-panel {position: absolute;top: 10px;left: 25%;z-index: 5;background-color: #fff;padding: 5px;border: 1px solid #999;text-align: center;font-family: \'Roboto\',\'sans-serif\';line-height: 30px;padding-left: 10px;}#floating-panel {background-color: #fff;border: 1px solid #999;left: 25%;padding: 5px;position: absolute;top: 10px;z-index: 5;}</style></head><body><div id=\"floating-panel\"><button onclick=\"toggleHeatmap()\">Toggle Heatmap</button><button onclick=\"changeGradient()\">Change gradient</button><button onclick=\"changeRadius()\">Change radius</button><button onclick=\"changeOpacity()\">Change opacity</button></div><div id=\"map\"></div><script>var map,heatmap;function initMap() {map = new google.maps.Map(document.getElementById('map'), {zoom: 13,center: {lat: 41.8, lng: -87.6},mapTypeId: 'satellite'});heatmap = new google.maps.visualization.HeatmapLayer({data: getPoints(),map: map});}function toggleHeatmap() {heatmap.setMap(heatmap.getMap() ? null : map);}function changeGradient() {var gradient = ['rgba(0, 255, 255, 0)','rgba(0, 255, 255, 1)','rgba(0, 191, 255, 1)','rgba(0, 127, 255, 1)','rgba(0, 63, 255, 1)','rgba(0, 0, 255, 1)','rgba(0, 0, 223, 1)','rgba(0, 0, 191, 1)','rgba(0, 0, 159, 1)','rgba(0, 0, 127, 1)','rgba(63, 0, 91, 1)','rgba(127, 0, 63, 1)','rgba(191, 0, 31, 1)','rgba(255, 0, 0, 1)']heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);}function changeRadius() {heatmap.set('radius', heatmap.get('radius') ? null : 20);}function changeOpacity() {heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);}function getPoints() {output = ["
        f.write(firstpart)
        with open("temp.txt","r+") as fi:
            reader = csv.reader(fi)
            first = True
            for row in reader:
                if first:
                      f.write("new google.maps.LatLng("+row[0]+","+row[1]+")")
                      first = False
                else:
                      f.write(",new google.maps.LatLng("+row[0]+","+row[1]+")")
        secondpart = "];return output;}</script><script async defersrc=\"https://maps.googleapis.com/maps/api/js?key=AIzaSyBmTUg4O2hqYtjaIksOPykzdiYkrGhVgME&libraries=visualization&callback=initMap\"></script></body></html>"
        f.write(secondpart)

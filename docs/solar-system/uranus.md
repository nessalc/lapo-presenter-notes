<script src="../../js/whatsup.js"></script>
<script src="../../js/utils.js"></script>
<script type="text/javascript">
	var objectName ="Uranus<br><h3>(YOUR-un-us)</h3>"
	var objectDesc ="7th Planet from the Sun<br/>The Sideways Planet"
	var objectImage="uranus.jpg"
</script>
<script type="text/javascript">
	setInterval(function(){
		fetch("../data.json")
			.then(function(response) {
				return response.json();
			})
			.then(function(data) {
				var d=new Date();
				var v=interpolate(data.Uranus.sun_distance,d.valueOf()/1000);
				document.getElementById("dist_sun").innerText=au_to_mi(v).numberFormat(3)+' miles';
				document.getElementById("dist_sun_au").innerText=v.numberFormat(3);
				var v=interpolate(data.Uranus.earth_distance,d.valueOf()/1000);
				document.getElementById("dist_earth").innerText=au_to_mi(v).numberFormat(3)+' miles';
				document.getElementById("dist_earth_light").innerText=au_to_ls(v).timeFormat()+' light-time';
				var v=data.Uranus.magnitude;
				document.getElementById("magnitude").innerText=v.numberFormat(2);
			})
			.catch(function(error) {
				console.log('error: '+error);
			});
		}, 1000);
</script>

|                                                                                         |                        |
| :-------------------------------------------------------------------------------------- | ---------------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Uranus](#uranus) | <div id=whatsup></div> |

# Uranus

Information about the planet Uranus.

|                                   |             Actual             |        Compared<br/>to Earth         |
| --------------------------------- | :-------------------------------------: | :--------------------------------------: |
| **Distance from Sun** (average)   |            1.8 billion miles            |                   19.2                   |
| **Distance from Sun** (current)   |  <span id="dist_sun">loading...</span>  | <span id="dist_sun_au">loading...</span> |
| **Distance from Earth** (current) | <span id="dist_earth">loading...</span><br /><span id="dist_earth_light">loading...</span> |                                        |
| **Magnitude** (current) | <span id="magnitude">loading...</span><br /> |                                        |
| **Revolution Period**             |                84 years                 |                                        |
| **Rotation Period**               |           17 hours 14 minutes           |                                        |
| **Diameter**                      |              31,900 miles               |                    4                     |
| **Mass**                          |                                       |                   14.5                   |
| **Surface Gravity**               |                                       |                  ~0.89                   |
| **Temperature** Cloud Tops        |        -200 &deg;C (-328 &deg;F)        |                                          |
| **Density** (gram/cubic cm)       |               1.30 gm/cm3               |                   0.24                   |

---

#### What To Look For Through The Telescope

---

1. Recommended eyepiece: 26mm or 40 mm.
2. Uranus appears as a small greenish ball through the telescope. None of its moons can be seen.

---

## Uranus Information

---

1. Uranus is the third largest planet in the solar system.
2. Uranus was the first planet discovered with a telescope – by William Herschel in 1781. It was plotted as a faint star on at least 20 star charts drawn between 1690 and 1781, but was not recognized as a planet.
3. Uranus rotates on its side as it orbits the sun. It is thought that a planet-sized body collided with Uranus early in the solar system’s history, causing Uranus to tip.
4. Uranus has a rocky core surrounded by a liquid mantle of water, ammonia, and methane. The outer layer is primarily hydrogen and helium with a small amount of methane.
5. The methane in Uranus’s atmosphere absorbs red light so we see the planet as blue-green.
6. The cloud features form beneath a layer of hydrocarbon smog and are almost invisible.
7. Ten very narrow rings circle Uranus. They are similar to the ringlets around Saturn. Another 50 very faint and very dusty rings were discovered by Voyager.
8. The rings around Uranus were discovered in 1977, by a team of astronomers watching Uranus pass in front of a distant star. This star seemed to blink out several times before Uranus itself covered the star – the rings were blocking the light from the star.
9. Uranus has at least 27 moons. They’re named mostly for characters from the works of Shakespeare and Alexander Pope.

|                                                                                                      |                |
| :--------------------------------------------------------------------------------------------------- | -------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Uranus](#uranus) > References | [Top](#uranus) |

###### References

| Item          | Updated | Notes                                                                                                    |
| ----------------- | ----------- | ------------------------------------------------------------------------------------------------------------ |
| Distance          | 2002-09-29  | <https://solarsystem.nasa.gov/planets/uranus/facts>                                                          |
| Revolution Period | 2017-05-07  | OK                                                                                                           |
| Rotation Period   | 2017-05-07  | OK                                                                                                           |
| Diameter          | 2017-05-07  | OK                                                                                                           |
| Mass              | 2017-05-07  | OK                                                                                                           |
| Surface Gravity   | 2017-05-07  | OK                                                                                                           |
| Temperature       | 2017-05-07  | OK                                                                                                           |
| Density           | 2017-05-07  | OK                                                                                                           |
| Other Information | 2017-05-07  | <https://nssdc.gsfc.nasa.gov/planetary/factsheet/uranusfact.html><br/><http://solarviews.com/eng/uranus.htm> |

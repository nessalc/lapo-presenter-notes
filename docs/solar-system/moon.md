<script src="../../js/whatsup.js"></script>
<script src="../../js/utils.js"></script>
<script type="text/javascript">
	var objectName ="The Moon"
    var objectDesc ="Earth's Satellite<br/>1 Lunar Day<br/><h6>706 frames, played at 24 fps = 29.45 seconds = ~1 lunar day"
	//var objectDesc ="Earth's Satellite"
    // var objectImage="moon.png" // Moon Phase Graphic
    // var objectImage="moon.jpg" // Moon
    // var objectImage="moon.gif" // Old animated moon
    var objectImage="lro-lunarday.gif" // new LRO animated moon
</script>
<script type="text/javascript">
	setInterval(function(){
		fetch("../data.json")
			.then(function(response) {
				return response.json();
			})
			.then(function(data) {
				var d=new Date();
				var v=interpolate(data.Moon.earth_distance,d.valueOf()/1000);
				document.getElementById("dist_earth").innerText=au_to_mi(v).numberFormat(3)+' miles';
				document.getElementById("dist_earth_light").innerText=au_to_ls(v).timeFormat()+' light-time';
			})
			.catch(function(error) {
				console.log('error: '+error);
			});
		}, 1000);
</script>

|   |   |
|:--|--:|
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Earth](/notes/#planets) > [Moon](#moon) | <div id=whatsup></div> |

# Moon

Information about Earth's Moon.

|                                    |                                         |                            |
| ---------------------------------- | :-------------------------------------: | :------------------------: |
|                                    |             <br/>**Actual**             | **Compared <br/>to Earth** |
| **Distance from Earth** (Average)  |              239,000 miles              |                            |
| **Distance from Earth** (Closest)  |              221,000 miles              |                            |
| **Distance from Earth** (Farthest) |              253,000 miles              |                            |
| **Distance from Earth** (Current)  | <span id="dist_earth">loading...</span><br /><span id="dist_earth_light">loading...</span> |             --             |
| **Revolution Period**              |                27.3 days                |                            |
| **Time from New Moon to New Moon** |                29.5 days                |             --             |
| **Diameter**                       |               2160 miles                |         1/4 (0.25)         |
| **Mass**                           |                                         |        1/81 (0.012)        |
| **Surface Gravity**                |           1.6 m/s<sup>2</sup>           |         1/6 (0.17)         |
| **Temperature** (Sunlight)         |         110 &deg;C (212 &deg;F)         |                            |
| **Temperature** (Shadow/Dark)      |        -180 &deg;C (-290 &deg;F)        |                            |
| **Density** (gram/cubic cm)        |         3.34 gm/cm<sup>3</sup>          |            0.61            |


---

#### What to look for through the telescope

---

1.  Recommended eyepiece:  26mm or 40mm

1.  People often wonder why the moon map is upside down. While they are looking through the finder, tell them to notice which side of the moon is light and which is dark. Have them do the same with their naked eye and they should realize that telescopes turn images upside down.

# Lunar Features

 - [Mare](../moon-mare)
 - [Craters](../moon-craters)
 - [Mountains](../moon-mountains)
 - [Other Features](../moon-other-features)


|                                                                                                                               |                           |
| :---------------------------------------------------------------------------------------------------------------------------- | ------------------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Earth](/notes/#planets) > [Moon](/notes/moon) > Lunar Phases | [top](#moon) |

# Lunar Phases

The phases of the Moon, in the sequence of their occurrence (from New Moon to New Moon):

|                                                                              |                                                                                                                                                                                                               |
| :--------------------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|        <img src="../../img/newmoon.gif" width="75" title="New Moon"/>        | **New Moon**<br/>(0% Illumination)<br/>The Moon's unilluminated side is facing the Earth.<br/>The Moon is not visible (except during a solar eclipse).                                                        |
| <img src="../../img/waxingcrescent.gif" width="75" title="Waxing Crescent"/> | **Waxing Crescent**<br/>(5-days old - 25%)<br/>The Moon appears to be partly but less than one-half illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is increasing.    |
|   <img src="../../img/firstquarter.gif" width="75" title="First Quarter"/>   | **First Quarter**<br/>(9 days old – 50%)<br/>One-half of the Moon appears to be illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is increasing.                        |
|  <img src="../../img/waxinggibbous.gif" width="75" title="Waxing Gibbous"/>  | **Waxing Gibbous**<br/>(13 days old – 75%)<br/>The Moon appears to be more than one-half but not fully illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is increasing  |
|       <img src="../../img/fullmoon.gif" width="75" title="Full Moon"/>       | **Full Moon**<br/>(15 days old – 100%)<br/>The Moon's illuminated side is facing the Earth.<br/>The Moon appears to be completely illuminated by direct sunlight.                                             |
|  <img src="../../img/waninggibbous.gif" width="75" title="Waning Gibbous"/>  | **Waning Gibbous**<br/>(19 days old – 75%)<br/>The Moon appears to be more than one-half but not fully illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is decreasing. |
|    <img src="../../img/lastquarter.gif" width="75" title="Last Quarter"/>    | **Last Quarter**<br/>(24 days old – 50%)<br/>One-half of the Moon appears to be illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is decreasing.                        |
| <img src="../../img/waningcrescent.gif" width="75" title="Waning Crescent"/> | **Waning Crescent**<br/>(29 days old – 25%)<br/>The Moon appears to be partly but less than one-half illuminated by direct sunlight.<br/>The fraction of the Moon's disk that is illuminated is decreasing.   |
|        <img src="../../img/newmoon.gif" width="75" title="New Moon"/>        | **New Moon**<br/>(29.5 days old - 0%)<br/>The Moon's unilluminated side is facing the Earth.<br/>The Moon is not visible (except during a solar eclipse).                                                     |
|                                                                              |                                                                                                                                                                                                               |

<p>Following Waning Crescent is New Moon, beginning a repetition of the complete phase cycle of 29.5-days average duration. The time in days counted from the time of New Moon is called the Moon's "age". Each complete cycle of phases is called a "lunation".</p>
source<a href="#footnote1" id="footnoteRef1"><sup>1</sup></a>

|                                                                                                                                    |                           |
| :--------------------------------------------------------------------------------------------------------------------------------- | ------------------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Earth](/notes/#planets) > [Moon](/notes/moon) > Features by Phase | [top](#moon) |

# Lunar Features by Phase

|                                                           |            |
| :-------------------------------------------------------- | ---------: |
| Waxing Crescent&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | (1-5 days) |
|                                                           |            |

- [Mare Crisium](../moon-mare#mare-crisium)
- [Altai Scarp](../moon-mare#altai-scarp)
- [Serpentine Ridge](moon-mare#serpentine-ridge)

|                                                                     |                |
| :------------------------------------------------------------------ | -------------: |
| First Quarter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | (6-9 days old) |
|                                                                     |                |

- [Mare Fecunditatis](../moon-mare#mare-fecunditatis)
- [Straight Wall](../moon-mare#straight-wall)

|                |                  |
| :------------- | ---------------: |
| Waxing Gibbous | (10-13 days old) |
|                |                  |

|                                                                 |                  |
| :-------------------------------------------------------------- | ---------------: |
| Full Moon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | (14-15 days old) |
|                                                                 |                  |

|                |                  |
| :------------- | ---------------: |
| Waning Gibbous | (16-19 days old) |
|                |                  |

|                                                              |                  |
| :----------------------------------------------------------- | ---------------: |
| Last Quarter&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | (20-24 days old) |
|                                                              |                  |

|                 |                  |
| :-------------- | ---------------: |
| Waning Crescent | (25-29 days old) |
|                 |                  |

|                                                                                                                                 |                           |
| :------------------------------------------------------------------------------------------------------------------------------ | ------------------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Earth](/notes/#planets) > [Moon](/notes/moon) > Apollo Program | [top](#moon) |

# Apollo Landing Sites

|             |               |              |                                             |
| ----------- | :-----------: | :----------: | :------------------------------------------ |
| **Mission** | **Longitude** | **Latitude** | **Location**                                |
| Apollo 11   | 23&deg; 29'E  | 00&deg; 40'N | just south of [Hypatia](../moon-craters#hypatia)|
| Apollo 12   | 23&deg; 24'W  | 03&deg; 12'S | north of the crater [Reinhold](../moon-craters#reinhold)|
| Apollo 14   | 17&deg; 28'W  | 03&deg; 40'S | southwest of the crater [Gambant](../moon-craters#gambant)|
| Apollo 15   | 03&deg; 39'E  | 26&deg; 06'N | between craters [Apianus](../moon-craters#apianus) and [Blanchinus](../moon-craters#blanchinus)|
| Apollo 16   | 15&deg; 31'E  | 09&deg; 00'S | southwest of the crater [Delambre](../moon-craters#delambre)|
| Apollo 17   | 30&deg; 31'E  | 20&deg; 10'N | in the crater [Fracastorius](../moon-craters#fracastorius) |
|             |               |              |                                             |

|                                                                                                                             |                           |
| :-------------------------------------------------------------------------------------------------------------------------- | ------------------------: |
| [Home](/notes/#object-notes) > [Solar System](/notes/#solar-system) > [Earth](/notes/#planets) > [Moon](/notes/moon) > References | [top](#moon) |

###### References

|                                                         |            |                                                    |
| ------------------------------------------------------- | ---------- | -------------------------------------------------- |
| <a id="footnote1" href="#footnoteRef1"><sup>1</sup></a> | 2017-04-17 | <http://aa.usno.navy.mil/faq/docs/moon_phases.php> |
|                                                         |            |                                                    |

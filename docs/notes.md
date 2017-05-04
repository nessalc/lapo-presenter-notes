# Presenter Notes

Object and Program notes for use during the public program at the<br/>
Lake Afton Public Observatory 16-inch telescope:

[TOC]


## Object Notes

### Solar System
- [The Sun](solar system/sun.md)

- #### Planets
    - [Mercury](solar system/mercury.md)
    - [Venus](solar system/venus.md)
    - ##### Earth
        - [The Moon](solar system/moon.md)
    - [Mars](solar system/mars.md)
    - [Jupiter](solar system/jupiter.md)
    - [Saturn](solar system/saturn.md)
    - [Uranus](solar system/uranus.md)
    - [Neptune](solar system/neptune.md)
- #### Asteroids
    - [Asteroids](solar system/asteroids/!asteroid_info.md)
    - [4 Vesta](solar system/asteroids/4vesta.md)
    - [Ceres](solar system/asteroids/ceres.md)
- #### Comets
    - [Comets](solar system/comets/!comet_info.md)
- #### Space Missions
    - [Missions](solar system/space missions/!missions_info.md)

### Galaxies
- #### Elliptical
    - [Elliptical Galaxies](galaxies/elliptical/!elliptical_galaxy_info.md)
    - [M49](galaxies/elliptical/m49.md)
    - [M84](galaxies/elliptical/m84.md)
    - [M85](galaxies/elliptical/m85.md)
    - [M87](galaxies/elliptical/m87.md)
- #### Irregular
    - [Irregular Galaxies](galaxies/irregular/!irregular_galaxy_info.md)
    - [M82](galaxies/irregular/m82.md)
- #### Spiral
    - [Spiral Galaxies](galaxies/spiral/!spiral_galaxy_info.md)
    - [M31](galaxies/spiral/m31.md)
    - [M51](galaxies/spiral/m51.md)
    - [M65](galaxies/spiral/m65.md)
    - [M66](galaxies/spiral/m66.md)
    - [M81](galaxies/spiral/m81.md)
    - [M94](galaxies/spiral/m94.md)
    - [M104](galaxies/spiral/m104.md)
    - [M106](galaxies/spiral/m106.md)
    - [NGC7331](galaxies/spiral/ngc7331.md)

### Nebulae
- #### Diffuse
    - [Diffuse Nebulae](nebulae/diffuse/!diffuse_nebulae_info.md)
    - [M17](nebulae/diffuse/m17.md)
    - [M42](nebulae/diffuse/m42.md)
- #### Planetary
    - [Planetary Nebulae](nebulae/planetary/!planetary_nebulae_info.md)
    - [M27](nebulae/planetary/m27.md)
    - [M57](nebulae/planetary/m57.md)
    - [NGC2392](nebulae/planetary/ngc2392.md)
    - [NGC3242](nebulae/planetary/ngc3242.md)
    - [NGC6826](nebulae/planetary/ngc6826.md)
- #### Supernovae Remnants
    - [Supernova Remnant](nebulae/supernovae_remnants/!supernova_remnant_info.md)
    - [M1](nebulae/supernovae_remnants/m1.md)
### Stars
##### Red
- [Giant](./stars/red/giant/!red_giant_stars.md)
    - [Aldebaran](./stars/red/giant/aldebaran.md)
    - [Arcturus](./stars/red/giant/arcturus.md)
    - [Capella](./stars/red/giant/capella.md)
    - [Pollux](./stars/red/giant/pollux.md)
    - [S Cephei](./stars/red/giant/s_cephei.md)
- [Super Giant](./stars/red/supergiant/!red_supergiant_stars.md)
    - [Antares](./stars/red/supergiant/antares.md)
    - [Betelgeuse](./stars/red/supergiant/betelgeuse.md)
    - [Mu Cephei](./stars/red/supergiant/mu_cephei.md)
##### [Yellow](./stars/yellow/!yellow_stars.md)
- [Beta Canes Venatici](./stars/yellow/beta_canes_venatici.md)
- [Beta Coma Berenices](./stars/yellow/beta_coma_berenices.md)
- [Procyon](./stars/yellow/procyon.md)
- [Xi Ursa Majoris](./stars/yellow/xi_ursa_majoris.md)
##### [Blue](./stars/blue/!blue_stars.md)
- [Altair](./stars/blue/altair.md)
- [Castor](./stars/blue/castor.md)
- [Deneb](./stars/blue/deneb.md)
- [Fomalhaut](./stars/blue/fomalhaut.md)
- [Regulus](./stars/blue/regulus.md)
- [Rigel](./stars/blue/rigel.md)
- [Sirius](./stars/blue/sirius.md)
- [Spica](./stars/blue/spica.md)
- [Vega](./stars/blue/vega.md)
##### Contrast Multiple
##### Contrast Optical Double
##### non-Contrast Multiple
##### non-Contrast Optical Double
##### with Planets


## Programs Notes

- Public thematic programs


## Notes on how to Edit and Maintain these documents

- To Be Completed...

## To Do Notes

Things to do to further prepare these notes...

- Get the vertical scroll working on the Left Nav Menu 
    -- fixed if needed.. just need to activate following CSS property...
    
    ``` css
    .bs-sidenav.well {
       overflow-x: auto;
    ```

- Implement a Javascript to enable/disable night vision mode by renaming the css/dayvision.css to nightvision.css...
this will work because the program only looks for the nightvision.css
and if it cannot find it... it defaults to the normal dayvision them.
If it does find the nightvision.css... then it enable the red on black for
the observing room.

    See https://www.thesitewizard.com/javascripts/change-style-sheets.shtml for example.

- Moon
    - link all object references between pages for quick navigation... e.g., "...in the crater [Fracastorius](#fracastorius)"

    - Alphabetize the moon objects and update the "by Phase" table with objects appropriate for the phase and cross-link all object references to the object entry

- Would like to get the fonts to match those of the LakeAfton.com site

- Customize the theme and document all necessary changes.

- Confirm that all links are active -- and review information they reference is accurate

- At initial deployment, should add a CNAME to the lakeafton.com domain host to point at
    the readthedocs.org site that is assigned for hosting the docs... e.g., 

    If you want the documentation on a subdomain point a CNAME record in your DNS to the subdomain for your project.

    For example, to make the documentation available on docs.lakeafton.com, create a CNAME record pointing to lakeafton-doc.readthedocs.org.

    CNAME   docs        is an alias of lakeafton-doc.readthedocs.org

- Fix the following errors during `mkdocs serve` (see source doc for commented warnings...)
<!--WARNING -  Template variable warning: 'page_description' is being deprecated and will not be available in a future version. 
            Use 'config.site_description' instead.
WARNING -  Template variable warning: 'site_author' is being deprecated and will not be available in a future version. 
            Use 'config.site_author' instead.
WARNING -  Template variable warning: 'canonical_url' is being deprecated and will not be available in a future version. 
            Use 'page.canonical_url' instead.
WARNING -  Template variable warning: 'favicon' is being deprecated and will not be available in a future version. 
            Use '{{ base_url }}/img/favicon.ico' instead.
WARNING -  Template variable warning: 'page_title' is being deprecated and will not be available in a future version. Use 'page.title' instead.
WARNING -  Template variable warning: 'site_name' is being deprecated and will not be available in a future version. Use 'config.site_name' instead.
WARNING -  Template variable warning: 'google_analytics' is being deprecated and  will not be available in a future version. 
            Use 'config.google_analytics' instead.
WARNING -  Template variable warning: 'current_page' is being deprecated and will not be available in a future version. Use 'page' instead.
WARNING -  Template variable warning: 'copyright' is being deprecated and will not be available in a future version. Use 'config.copyright' instead.
WARNING -  Template variable warning: 'include_nav' is being deprecated and will not be available in a future version. Use 'nav|length>1' instead.
WARNING -  Template variable warning: 'include_next_prev' is being deprecated and will not be available in a future version. 
            Use '(page.next_page or page.previous_page)' instead.
WARNING -  Template variable warning: 'repo_url' is being deprecated and will not be available in a future version. Use 'config.repo_url' instead.
WARNING -  Template variable warning: 'homepage_url' is being deprecated and will not be available in a future version. Use 'nav.homepage.url' instead.
WARNING -  Template variable warning: 'previous_page' is being deprecated and will not be available in a future version. Use 'page.previous_page' instead.
WARNING -  Template variable warning: 'next_page' is being deprecated and will not be available in a future version. Use 'page.next_page' instead.
WARNING -  Template variable warning: 'repo_name' is being deprecated and will not be available in a future version. Use 'config.repo_name' instead.
WARNING -  Your theme does not appear to contain a 'main.html' template. The 'base.html' template was used instead, which is deprecated. 
            Update your theme so that the primary entry point is 'main.html'.
WARNING -  Template variable warning: 'toc' is being deprecated and will not beavailable in a future version. Use 'page.toc' instead.
WARNING -  Template variable warning: 'meta' is being deprecated and will not be available in a future version. Use 'page.meta' instead.
WARNING -  Template variable warning: 'content' is being deprecated and will not be available in a future version. Use 'page.content' instead.-->

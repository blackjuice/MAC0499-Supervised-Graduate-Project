# MAC0499 - Supervised Graduate Project

*version*: `Blender 2.76b`

Forensic facial reconstruction on criminal cases using Blender as main software.

## Contents

* [Tasks](#todo)
* [Steps used](#steps)
* [Landmarks](#landmarks)
* [Subjects](#subjects)
* [MakeHuman](#mkhuman)
* [Addons](#addons)
* [References](#references)

<a name="todo"></a>
## Tasks

- [ ] 00. Fix parameters
- [ ] 01. SKULL
  - [ ] 01.0. import *.stl* subject
  - [ ] 01.1. Simplify:
    - [ ] 01.1.0. clean up skull by deleting faces
    - [ ] 01.1.1. `DECIMATE` addon: lower ratio at **Collapse**
  - [ ] 01.2. Align:
    - [ ] 01.2.0. set origin to Center of Mass
    - [ ] 01.2.1. align horizontally and vertically
  - [ ] 01.
  - [ ] asdasd

<a name="addons"></a>
## Addons

Directory for the addons:

```bash
\276b\2.76\scripts\addons
```

Activate `Import-Export: Import: MakeHuman(.mhx)` and `Rigging: Rigify`

<a name="mkhuman"></a>
## MakeHuman

*Version*: `1.1.0`

<a name="subjects"></a>
## Subjects

| subject | gender  | age | group     |
|:--------|:--------|:----|:----------|
| Mariza  | female  | 49  | caucasian |
| Eduardo | male    | 24  | caucasian |
| Felipe  | male    | 21  | caucasian | *
| Bruna   | male    | 22  | caucasian |

<a name="landmarks"></a>
## Landmarks

| Midline points      | Bilateral points      |
|:--------------------|:----------------------|
| 1. Supraglabella    | 11. Frontal eminence  |
| 2. Glabella         | 12. SupraOrbital      |
| 3. Nasion           | 13. Suborbital        |
| 4. Rhinion          | 14. Inferior Malar    |
| 5. Mid-philtrum     | 15. Lateral orbit     |
| 6. Supradentale     | 16. Zygomatic arch    |
| 7. Infradentale     | 17. Supraglenoid      |
| 8. Supramentale     | 18. Gonion            |
| 9. Mental eminence  | 19. SupraM2           |
| 10. Menton          | 20. Occlusal line     |
|                     | 21. SubM2             |

<a name="steps"></a>
## Steps

1. Import/Align skull

* import stl file;
* Set origin to Center of Mass;
* Align skull on X axis;

2. Simplify skull

* Delete unnecessary faces
* Add modifier: Decimate
    * at Collapse: lower the ratio to 0.1 (result: from 725623 to 72562)

3. Import MakeHuman template

* Import *sleep* expression

4. Manipulate MakeHuman template

* Delete unnecessary faces
* Add rig to close mouth

Placing tops

* Add armature;
* Activate `Snap during transformation` or `Shift + Tab`
* Activate `Align rotation with the snapping target`

It could...

* align horizontally and vertically the head position for the modelling;
* low the polygons on the skull mesh by drawing a low pol object;


<a name="references"></a>
## References

* https://tutsplus.com/
* https://tutsplus.com/
* http://www.amazon.com/Facial-Expressions-Visual-Reference-Artists/dp/0823016714/ref=sr_1_1?ie=UTF8&qid=1457657754&sr=8-1&keywords=facial+expressions
* http://www.amazon.com/Two--Three-Dimensional-Patterns-Peter-Hallinan/dp/1568810873/ref=sr_1_1?ie=UTF8&qid=1457714856&sr=8-1&keywords=two+and+three+dimensional+patterns+of+the+face
* http://www.scielo.br/scielo.php?script=sci_arttext&pid=S1517-74912003000100005
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4606364/
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2815945/
* https://www.omicsonline.org/scholarly/forensic-facial-reconstruction-journals-articles-ppts-list.php
* http://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=1005&context=anthr_symposium
* https://archives.fbi.gov/archives/about-us/lab/forensic-science-communications/fsc/jan2001/phillips.htm
* http://delivery.acm.org/10.1145/890000/882307/p554-kahler.pdf?ip=143.107.44.18&id=882307&acc=ACTIVE%20SERVICE&key=4D4702B0C3E38B35.4D4702B0C3E38B35.CAD1463F6EF63783.4D4702B0C3E38B35&CFID=703274842&CFTOKEN=11730693&__acm__=1481548127_a72993439f72ce698166a65bc8368291

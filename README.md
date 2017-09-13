# MAC0499 - Supervised Graduate Project

Forensic facial reconstruction on criminal cases using Blender as main software.

## Contents

* [Tasks](#todo)
* [Subjects](#subjects)
* [Softwares](#softwares)
* [Landmarks](#landmarks)
* [Steps used](#steps)
* [References](#references)

<a name="todo"></a>
## Tasks

#### 00. There are still minor fixes left to be addressed:

- [ ] 00. Fix parameters

#### 01. **Landmark process**. This step manipulates only the imported skull:

- [ ] 01. **MANIPULATOR**: the *.stl* imported file of the skull must go through a clean up, lowering number of polygons for light manipulation
  - [ ] 01.0. Simplify:
    - [ ] 01.0.0. clean up skull by deleting faces
    - [ ] 01.0.1. `DECIMATE` tool: lower ratio to 0.1, at **Collapse**
  - [ ] 01.1. Alignment:
    - [ ] 01.1.0. set origin to Center of Mass
    - [ ] 01.1.1. align mesh along X, Y, Z axis
- [ ] 02. **LANDMARK** - COORDINATES: After having a more lighter version of the skull, the mesh must go under a heavy points' analysis.
  - [ ] 02.0. Manual analysis: must be our first approach. The user will be the one who will position and identify landmark points.
  - [ ] 02.1. *Automatic*: skull must go through a point analysis, giving us a table containing all the landmark coordinates throughout the skull, with horizontal planes such as the Frankfurt plane. With all the data ready, Blender must print the data on the skull for the user.
- [ ] 03. **LANDMARK** - GENERATOR: user gives an input containing 2 informations: *gender* and *group* of the subject
  - [ ] 03.0. Input box: there must be a toolbar box on the interface that receives the 3 parameters
  - [ ] 03.1. *generator( gender, group )*: `Python` script that receives 2 parameters and returns 31 landmark cylinders, all named, grouped and colored
- [ ] 04. **LANDMARK** - POSITIONING: having all coordinates of the landmarks on the skull and the landmarks cylinders, ready to be placed, this step returns the skull with positioned landmarks

#### 02. **Skin process**. This step generates and manipulates the head generated from MakeHuman. We will call the generated head as *skin*.

- [ ] 05. **MAKEHUMAN v.1.1.0**:
  - [ ] 05.0. Engine: Figure out how to use MakeHuman without needing to open the software
  - [ ] 05.1. Head extraction: user gives an input containing 3 inputs: *age*, *gender* and *group* of the subject. After generating the character, we need to know how to extract the head only
  - [ ] 05.2. Simplify: the extracted head of the generated character must undergo a clean up, such as deleting unnecessary faces of the mesh
- [ ] 06. **ARMATURE**: the skin now also have to be heavily analyzed
  - [ ] 06.0. Alignment: similar to `01.1.`
  - [ ] 06.1. Rigging: skin will be heavily rigged. Analysis must be executed in order to identify where the bones (of the armature) should be correctly placed for the deformation process.
- [ ] 07. **Deformation process**. This step will combine the skin generated with the skull, which contains all the anatomical information. With this last process, the subject with the facial reconstructed will be ready for evaluation.
  - [ ] 07.0. Snap: landmark bones of the armature from the skin will be snapped to the landmark points/positions/cylinders

<a name="subjects"></a>
## Subjects

Currently, there are 4 subjects that must go under reconstruction. 3 main characteristics are crucial data: gender, age and group of the subject.

| subject | gender  | age | group     |
|:--------|:--------|:----|:----------|
| Mariza  | female  | 49  | caucasian |
| Eduardo | male    | 24  | caucasian |
| Felipe  | male    | 21  | caucasian | *
| Bruna   | male    | 22  | caucasian |


<a name="softwares"></a>
## Softwares

### Blender

*version*: `Blender 2.76b`

Directory for the addons:

```bash
\276b\2.76\scripts\addons
```

The Blender 2.76b version supports MakeHuman tools. It's necessary to activate the following: `Import-Export: Import: MakeHuman(.mhx)` and `Rigging: Rigify`.

### MakeHuman

*Version*: `1.1.0`

Future version of the research must use MakeHuman as an engine instead of a standalone.

<a name="landmarks"></a>
## Landmarks

There are 2 main layer of points and 31 landmark points.

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
* write addon: https://docs.blender.org/api/blender_python_api_2_65_5/info_tutorial_addon.html
* python example blender: https://wiki.blender.org/index.php/Doc:2.4/Manual/Extensions/Python/Example
* simple panel removal: http://blender.stackexchange.com/questions/19249/simplify-blender-gui-using-python
* blender org python: https://www.blender.org/forum/viewforum.php?f=9
* blender org interface: https://www.blender.org/forum/viewforum.php?f=8
* blender doc: https://docs.blender.org/api/249PythonDoc/
* fluid designer Modifying Blenders UI: https://www.youtube.com/watch?v=C8xcR-kF7X8
* fluid designer source code: https://github.com/Microvellum/Fluid-Designer
* Setting up Eclipse for Blender Python Debugging: https://www.blendernation.com/2013/09/25/setting-up-eclipse-for-blender-python-debugging/
* Python, Blender and a bit of debuggery: http://daniepstein.com/daniepstein/tutorials/python-blender-and-a-bit-of-debuggery/

enable addon through scripts

* How to enable and disable Add-ons via Python?: http://blender.stackexchange.com/questions/32409/how-to-enable-and-disable-add-ons-via-python

3D wrapping methods:

* 3D Convex Hull (CGAL)

3D Face Recognition without Facial Surface
Reconstruction

* http://www.face-rec.org/algorithms/3d_morph/cis-2003-05.pdf

keyword: Feature detection

* http://www.cs.technion.ac.il/~ron/PAPERS/BroBroKimIJCV05.pdf

stl files

* https://exploreideasdaily.wordpress.com/tag/stl-files/

Add-ons Development

* https://wiki.blender.org/index.php/Dev:Py/Scripts

Video basic addon template

* https://www.youtube.com/watch?time_continue=526&v=OEkrQGFqM10

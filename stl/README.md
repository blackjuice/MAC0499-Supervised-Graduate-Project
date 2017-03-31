# dot stl

*source: https://en.wikipedia.org/wiki/STL_(file_format)*

An STL file describes a raw unstructured triangulated surface by the unit normal and vertices (ordered by the right-hand rule) of the triangles using a three-dimensional Cartesian coordinate system. STL coordinates must be positive numbers, there is no scale information, and the units are arbitrary.

## ASCII STL

An ASCII STL file begins with the line
    
    solid name

where name is an optional string (though if name is omitted there must still be a space after solid). The file continues with any number of triangles, each represented as follows:

    facet normal ni nj nk
        outer loop
            vertex v1x v1y v1z
            vertex v2x v2y v2z
            vertex v3x v3y v3z
        endloop
    endfacet

where each n or v is a floating-point number in sign-mantissa-"e"-sign-exponent format, e.g., "2.648000e-002" (noting that each v must be non-negative). The file concludes with

    endsolid name

The structure of the format suggests that other possibilities exist (e.g., facets with more than one "loop", or loops with more than three vertices). In practice, however, all facets are simple triangles.
White space (spaces, tabs, newlines) may be used anywhere in the file except within numbers or words. The spaces between "facet" and "normal" and between "outer" and "loop" are required

##  Binary STL

Because ASCII STL files can become very large, a binary version of STL exists. A binary STL file has an 80-character header (which is generally ignored, but should never begin with "solid" because that will lead most software to assume that this is an ASCII STL file). Following the header is a 4-byte unsigned integer indicating the number of triangular facets in the file. Following that is data describing each triangle in turn. The file simply ends after the last triangle.

Each triangle is described by twelve 32-bit floating-point numbers: three for the normal and then three for the X/Y/Z coordinate of each vertex – just as with the ASCII version of STL. After these follows a 2-byte ("short") unsigned integer that is the "attribute byte count" – in the standard format, this should be zero because most software does not understand anything else.

Floating-point numbers are represented as IEEE floating-point numbers and are assumed to be little-endian, although this is not stated in documentation.

    UINT8[80] – Header
    UINT32 – Number of triangles

    foreach triangle
    REAL32[3] – Normal vector
    REAL32[3] – Vertex 1
    REAL32[3] – Vertex 2
    REAL32[3] – Vertex 3
    UINT16 – Attribute byte count
    end

## The facet normal

In both ASCII and binary versions of STL, the facet normal should be a unit vector pointing outwards from the solid object. In most software this may be set to (0,0,0), and the software will automatically calculate a normal based on the order of the triangle vertices using the "right-hand rule". Some STL loaders (e.g. the STL plugin for Art of Illusion) check that the normal in the file agrees with the normal they calculate using the right-hand rule and warn the user when it does not. Other software may ignore the facet normal entirely and use only the right-hand rule. Although it is rare to specify a normal that cannot be calculated using the right-hand rule, in order to be entirely portable, a file should both provide the facet normal and order the vertices appropriately. A notable exception is SolidWorks, which uses the normal for shading effects.

## Handling .stl in Blender

*source: https://www.stratasysdirect.com/resources/how-to-prepare-stl-files/*

Prior to exporting, ensure your object is uniform by checking that all surfaces/ vertices are connected.

To check your file for uniformity:

1. Enter Edit Mode, select your object, and press “L” over the mesh
  1.0. Areas that do not highlight are free-floating. All vertices must be connected for your part to print.
2. After you’ve confirmed your object is uniform, check for holes in the mesh of your part
3. Enter Edit Mode, deselect all vertices, and select Non Manifold from the drop down menu or simply hit Shft-Ctrl-Alt-M
4. Change the units and dimensions of your object
  4.0. Blender’s default measurement is called a Blender Unit and is equal to one meter
  4.1. Press “N” to bring up your dimensions tab
  4.2. Change units from Blender Units to Metric by selecting Properties > Scene Tab
  4.3. Change units to Metric (preferably millimeter)
  4.4. Adjust your scale within the dimensions tab to compute with Metrics

Now your file is ready for export.

1. Select `File > Export as .STL (* .stl)`

Tip: Modifiers can be applied during export or prior.
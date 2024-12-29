<h1 align="center"> 📋Project 1</h1>

### 📌 Folder Structure must be follows:

<!-- ![Folder Structure](./rough/image.png) -->

<img src="./rough/image.png" alt="Folder Structure">

<p>Data folder is not available on GitHub. You need to download it.
<a href="https://drive.google.com/drive/folders/185s6GPg_lCsxFv08o4BXslnWhguH9wIt?usp=drive_link">Click</a>
</p>


<h3 align = "center" > 1️⃣ Plot Full Map of India Using `.xyz` or `.txt` File</h3>

---

<img align ="right" src="./plots/Full%20image%20of%20india%20Topography.png" alt="Full Map of India Topography" width="300px">

- convert `.txt` to `.csv` file
- save csv file
- fixed the region 
- plot

<br>
<br>   
<br>   
<br> 
<br>
<br>   
<br>   
<br> 


<h3 align = "center" > 2️⃣ Plot Land Portions of India</h3>

---

<div style="text-align: center;">
    <img align = "right" src="./plots/croped%20image%20of%20india%20land.png" alt="Full Map of India Topography" width="300px">
</div>


This project involves plotting the land portions of India using topographic data provided in a `.txt` or `.xyz` file.and clip usnig `boundary.geojson` file:

- **Cropping Land Portion**: Use a GeoJSON file to crop and focus on India's land portion.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<!-- 2. **Water Portion Plotting**: Plot the water portion separately. -->
<!-- 3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features. -->
<!-- 4. **Merging Plots**: Merge the land and water plots together. (Note: Nepal, China, Bhutan, and Bangladesh are not included in the plot.) -->

<!-- -------------------------------------------------------------- -->
<h3 align = "center" >3️⃣ Plot water Portions of India</h3>

---

This project involves plotting the land portions of India using topographic data provided in a `.csv` file.and clip usnig `World_Seas_IHO_v3.shp` file:
<br>
<img align="right" src="./plots/croped image of india water.png" alt="water shape" width = "300px">
- **Plot shp file**: Plot the shapefile of water portion of India.</br>
    - first open the file in `geopandas`
    - create base map
    - fix the region
    - plot the figure
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<img align = "right" src="./rough/output.png" alt="land" width = "300px">

- **Cropping water Portion**: Use a `.shp` file to crop and focus on India's water portion.
- **Water Portion Plotting**: Plot the water portion separately.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<!-- 3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features. -->
<!-- 4. **Merging Plots**: Merge the land and water plots together. (Note: Nepal, China, Bhutan, and Bangladesh are not included in the plot.) -->
<div style="text-align: center;justify-content:center; display:flex;width:300px;  margin: 0 auto;">
    
</div>
<!-- ---------------------------------------------------------------------------------------------------------------------- -->
<h3 align = "center" >4️⃣ Merge the land and water portion of India</h3>

---

<img align = "right" src="./rough/merged.png" alt="land" width="300px">
Simply using `pillow` module we do it.(this is a shortcut process otherwise you can use geojson file to crop it)

> **Transparent image**: Firstly we make transparent the `croped image of india water.png` and `croped image of india land.png`.</br>
>**Merge them**: Using `pillow` module we merge them .</br>
>**plot** : using `pygmt` finally we plot the merged image</br>

<div style="text-align: center; width:300px; margin: 0 auto;">
    
</div>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<h1 align = "center">Thank You </h1>


---


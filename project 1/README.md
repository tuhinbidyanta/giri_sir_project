<h1 align="center"> 📋Project 1</h1>

### Folder Structure must be follows:

<!-- ![Folder Structure](./rough/image.png) -->

<img src="./rough/image.png" alt="Folder Structure">

<p>Data folder is not available on GitHub. You need to download it.
<a href="https://drive.google.com/drive/folders/185s6GPg_lCsxFv08o4BXslnWhguH9wIt?usp=drive_link">Click</a>
</p>


<h3 align = "center" >Plot Full Map of India Using `.xyz` or `.txt` File</h3>

---

<img align ="right" src="./plots/Full%20image%20of%20india%20Topography.png" alt="Full Map of India Topography" width="300px">

- convert `.txt` to `.csv` file
- save csv file
- fixed the region 
- plot
```python
file_path = "./data/topographic_data_india.csv"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")
    df = pd.read_csv("./data/topography_data_india.txt", delim_whitespace=True)
    df.to_csv("./data/topographic_data_india.csv", index=False,header=['longitude','latitude','depth'])
    print("csv convertion successfull!")
```
$$\text{}$$
$$\text{}$$
$$\text{}$$
$$\text{}$$
$$\text{}$$
$$\text{}$$   


<h3 align = "center" >Plot Land Portions of India</h3>

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
<h3 align = "center" >Plot water Portions of India</h3>

---

This project involves plotting the land portions of India using topographic data provided in a `.csv` file.and clip usnig `World_Seas_IHO_v3.shp` file:
- **Plot shp file**: Plot the shapefile of water portion of India.</br>

> **Cropping water Portion**: Use a `.shp` file to crop and focus on India's water portion.</br>
> **Water Portion Plotting**: Plot the water portion separately.
<!-- 3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features. -->
<!-- 4. **Merging Plots**: Merge the land and water plots together. (Note: Nepal, China, Bhutan, and Bangladesh are not included in the plot.) -->
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img style="padding:20px" src="./plots/croped image of india water.png" alt="water shape" width = "300px">  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<img style="padding:20px" src="./rough/output.png" alt="land" width = "300px">
<div style="text-align: center;justify-content:center; display:flex;width:300px;  margin: 0 auto;">
    
</div>
<!-- ---------------------------------------------------------------------------------------------------------------------- -->
<h3 align = "center" >Merge the land and water portion of India</h3>

Simply using `pillow` module we do it.(this is a shortcut process otherwise you can use geojson file to crop it)

> **Transparent image**: Firstly we make transparent the `croped image of india water.png` and `croped image of india land.png`.</br>
>**Merge them**: Using `pillow` module we merge them .</br>
>**plot** : using `pygmt` finally we plot the merged image</br>

<div style="text-align: center; width:300px; margin: 0 auto;">
    <img src="./rough/merged.png" alt="land" width="300px">
</div>

<h1>Thank You </h1>


---


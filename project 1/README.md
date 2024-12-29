<h1 style="text-align: center;">Project 1</h1>


### Folder Structure must be follows:

<!-- ![Folder Structure](./rough/image.png) -->
<div style="text-align: center;">
    <img src="./rough/image.png" alt="Folder Structure">
</div>
<p>Data folder is not available on GitHub. You need to download it.
<a href="https://drive.google.com/drive/folders/185s6GPg_lCsxFv08o4BXslnWhguH9wIt?usp=drive_link">Click</a>
</p>

<h3 style = "background-color :black; border-radius:10px; color :white; padding:5px;" >Plot Full Map of India Using `.xyz` or `.txt` File</h3>
This project involves plotting the map of India using topographic data provided in a `.txt` or `.xyz` file. The data is first converted to a CSV format and then visualized using PyGMT

> **Data Conversion**: Convert the text data to CSV format for easier manipulation.</br>
> **Full Map Plotting**: Plot the entire map of India using the CSV data.</br>

<div style="text-align: center; width:300px; margin: 0 auto;">
    <img src="./plots/Full image of india Topography.png" alt="Fo">
</div>
<!-- --------------------------------------------------------- -->
<h3 style = "background-color :black; border-radius:10px; color :white; padding:5px;" >Plot Land Portions of India</h3>

This project involves plotting the land portions of India using topographic data provided in a `.txt` or `.xyz` file.and clip usnig `boundary.geojson` file:

> **Cropping Land Portion**: Use a GeoJSON file to crop and focus on India's land portion.
<!-- 2. **Water Portion Plotting**: Plot the water portion separately. -->
<!-- 3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features. -->
<!-- 4. **Merging Plots**: Merge the land and water plots together. (Note: Nepal, China, Bhutan, and Bangladesh are not included in the plot.) -->
<div style="text-align: center; width:300px; margin: 0 auto;">
    <img src="./plots/croped image of india land.png" alt="land">
</div>
<!-- -------------------------------------------------------------- -->
<h3 style = "background-color :black; border-radius:10px; color :white; padding:5px;" >Plot water Portions of India</h3>

This project involves plotting the land portions of India using topographic data provided in a `.csv` file.and clip usnig `World_Seas_IHO_v3.shp` file:

> **Plot shp file**: Plot the shapefile of water portion of India.</br>
> **Cropping water Portion**: Use a `.shp` file to crop and focus on India's water portion.</br>
> **Water Portion Plotting**: Plot the water portion separately.
<!-- 3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features. -->
<!-- 4. **Merging Plots**: Merge the land and water plots together. (Note: Nepal, China, Bhutan, and Bangladesh are not included in the plot.) -->

<div style="text-align: center;justify-content:center; display:flex;width:300px;  margin: 0 auto;">
    <img style="padding:20px" src="./plots/croped image of india water.png" alt="water shape">
    <img style="padding:20px" src="./rough/output.png" alt="land">
</div>
<!-- ---------------------------------------------------------------------------------------------------------------------- -->
<h3 style = "background-color :black; border-radius:10px; color :white; padding:5px;" >Merge the land and water portion of India</h3>

Simply using `pillow` module we do it.(this is a shortcut process otherwise you can use geojson file to crop it)

> **Transparent image**: Firstly we make transparent the `croped image of india water.png` and `croped image of india land.png`.</br>
>**Merge them**: Using `pillow` module we merge them .</br>
>**plot** : using `pygmt` finally we plot the merged image</br>

<div style="text-align: center; width:300px; margin: 0 auto;">
    <img src="./rough/merged.png" alt="land">
</div>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Thank You</title>
  <style>
    body {
      font-family: 'Arial', sans-serif;
      
    }

    .thank-you {
      text-align: center;
      animation: fadeIn 4s infinite ease-in-out;
    }

    .thank-you h1 {
      font-size: 4rem;
      margin: 0;
      letter-spacing: 5px;
      text-transform: uppercase;
      background: linear-gradient(90deg, #f39c12, #e74c3c, #8e44ad);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    


    @keyframes fadeIn {
      0% {
        opacity: 0;
        transform: translateY(20px);
      }
      50% {
        opacity: 1;
        transform: translateY(0);
      }
      100% {
        opacity: 0;
        transform: translateY(20px);
      }
    }
  </style>
</head>
<body>
  <div class="thank-you">
    <h1>Thank You Sir</h1>
  </div>
</body>
</html>

---


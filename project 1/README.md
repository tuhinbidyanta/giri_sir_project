<h1 style="text-align: center;">Project 1</h1>


### plot full map of india using `.xyz` or `.txt` file given on topography_data_india.txt
This project involves plotting the map of India using topographic data provided in a `.txt` or `.xyz` file. The data is first converted to a CSV format and then visualized using PyGMT. The steps include:

1. **Data Conversion**: Convert the text data to CSV format for easier manipulation.
2. **Full Map Plotting**: Plot the entire map of India using the CSV data.

### plot land and and water portion of india using `.xyz` or `.txt` file given on topography_data_india.txt and finally merge the two plots together( caution : nepal and china ,bhutan and bangladesh are not included the plot )
This project involves plotting the land and water portions of India using topographic data provided in a `.txt
1. **Cropping Land Portion**: Use a GeoJSON file to crop and focus on India's land portion.
3. **Shapefile Integration**: Integrate shapefiles to enhance the map with additional geographical features.

---
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Folder Structure</title>
    <style>
        ul {
            list-style-type: none;
        }
        li::before {
            content: "├── ";
            color: #333;
        }
        li:last-child::before {
            content: "└── ";
        }
    </style>
</head>
<body>
    <h1>Project Folder Structure</h1>
    <ul>
        <li>project 1
            <ul>
                <li>__pycache__</li>
                <li>data</li>
                <li>image manipulation</li>
                <li>plots</li>
                <li>imageplot.py</li>
                <li>main.ipynb</li>
                <li>project.md</li>
            </ul>
        </li>
    </ul>
</body>
</html>

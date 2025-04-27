# :mortar_board: Graduate admission data app

This data app assists in evaluating students' chances of gaining admission to any college in the USA. The data is utilized to train a model within this 
<a href="https://github.com/noor188/Graduate-Admission-Prediction">project</a>.

View the app: <a href="https://github.com/noor188/Graduate-Admission-Prediction">Preswald data app</a>

--- 

## Dashboard Overview

- Includes 5 metrics: GRE, TOEFL, CGPA, research, and university rating
- Utilizes sample data for analysis
- Visualizes data with histograms for each metric
- Investigates correlations between the final metric and each individual value

--- 

## Technology

- Programming language: Python
- Libraries: pandas, plotly, matplotlib, numpy
- Frameworks: <a href="https://github.com/StructuredLabs/preswald">Preswald </a>open source<br>

--- 

## Run this App (The fun part—see it in action!)

The <a href="https://github.com/noor188/Graduate-Admission-Prediction">app</a> is hosted on the Perswald platform, but it can be hosted locally.
Run the app locally with:

```bash
preswald run
```

This command launches a development server, and Preswald will let you know where your app is hosted. Typically, it’s here:

```
🌐 App running at: http://localhost:8501
```

Open your browser, and voilà—your Preswald app is live!

--- 

## My Overview of the Perswald Framework

### What I liked:

- The framework is thoroughly documented
- The use of a DAG to track user input dynamically and update the dashboard in real-time
- The ability to create an app with just a few lines of code!

### My suggestions:

- Provide clearer guidance on utilizing the dynamic UI (for example, slider, select input, etc.)
- Implement a logging system to track errors

--- 

## Project Structure
```
/
├── hello.py (run code)
├── preswald.toml (configuration)
├── data/
|   ├── graduate_admission.csv
├── images/
|   ├── favicon.ico
|   ├── logo.png 
└──
```


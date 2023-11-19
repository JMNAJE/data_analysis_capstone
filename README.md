data_analysis_capstone.

# data_analysis_capstone

<img src="https://logos-world.net/wp-content/uploads/2023/08/MLB-Logos-30-Major-League-Baseball-Team-Logos-and-Names.png?resize=930%2C620&ssl=1" alt="ACNH image" width="500" height="300">

## About

In this analysis of the 2018 Major League Baseball (MLB) season, I examined the performance metrics of both teams and individual players. Our primary focus revolved around identifying correlations between the top-performing players and the overall success of their respective teams. By delving into key statistical categories such as Runs, Hits, Home Runs, and Wins, W aimed to uncover insights into what factors most significantly contributed to team victories and, ultimately, postseason achievements.

## Data Sources

CSVs:<br><br>
<b>atbats.csv</b>
This dataset contains the names of Major League Baseball players along with the number of games played, at-bats, runs, hits, and other measurable statistics for the 2018 season.

<b>teams.csv</b>
This dataset captures the statistics of all 30 Major League Baseball teams for the 2018 season. It includes team stats such as total wins and losses. Additionally, it encompasses overall team performance metrics such as runs, hits, home runs, and strikeouts.

## Virtual Environment Installation

Before you start to explore the project, please ensure you have met the following requirements:

- You have installed Python. This project was developed using Python 3.11.1. If you don't have Python installed or if you need to upgrade your current version, you can download it from the [official Python website](https://www.python.org/downloads/).
- You have installed Git, which is necessary to clone the repository. If you don't have Git installed, you can download it from the [official Git website](https://git-scm.com/downloads).

Follow these steps to run the project on your local machine:

1. **Clone the repository**

   Navigate to the directory where you want the cloned repository to be placed by using the ``cd`` command in your terminal, followed by the path of the directory.

   Then, you can clone this repository by running the following command in your terminal:

   git clone https://github.com/JMNAJE/data_analysis_capstone.git
2. **Navigate to the cloned directory**

   Change your current directory to the cloned repository's directory data_analysis_capstone.
3. **Set up a virtual environment**

   Creating a virtual environment is recommended to keep the project's dependencies isolated from your system's Python environment. You can create a virtual environment using the following command:

   On Windows:

   ```
   python -m venv venv
   ```

   On macOS and Linux:

   ```
   python3 -m venv venv
   ```

   This will create a new virtual environment named `venv` in your current directory.
4. **Activate the virtual environment**

   Activate the virtual environment using the following command:

   On Windows:

   ```
   .\venv\Scripts\activate
   ```

   On macOS and Linux:

   ```
   source venv/bin/activate
   ```

   Your prompt should change to indicate that you are now operating within a Python virtual environment.
5. **Install the required packages**

   Install the required packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

   You're now ready to run the project!
6. **Run the ``data_analysis_capstone.ipynb`` file:**

   - If you have Jupyter Notebook installed, enter ``jupyter notebook`` and open the `.ipynb` file.
   - If you are using Visual Studio Code, open the `.ipynb` file and run the cells using the run button that appears at the top left of each cell.

To deactivate the virtual environment when you're done, simply type `deactivate` in your terminal.

## Data Visualizations
Futher data exploration and visualizations can be found on [Tableau Public Work](https://public.tableau.com/app/profile/jose.najera4967/viz/data_analysis_capstone_Tableau/2018MLBDashboard)


## Summary of Findings

Historically, teams with a strong offensive lineup, like the 2018 Boston Red Sox, have shown success in the postseason. The Red Sox's victory in the 2018 World Series, backed by their players' high rankings in key batting statistics, exemplifies this trend. However, it's important to note that while this is a supportive factor, it's not an absolute predictor.

The contrasting postseason fates of the 2018 Milwaukee Brewers and Los Angeles Dodgers encapsulate the unpredictable nature of baseball playoffs. While the Brewers, leading the National League in regular-season wins, did not advance to the World Series, the Dodgers made it to the finals despite having fewer wins and lacking top-10 players in key statistics. This dichotomy highlights that success in baseball is not solely contingent on regular-season performance or individual statistical dominance. Factors like playoff experience, team depth, balanced contributions across the roster, strategic in-game decisions, and effective bullpen management play pivotal roles in navigating the intricacies and pressures of postseason baseball, often overriding regular-season achievements.

The 2018 Milwaukee Brewers and Los Angeles Dodgers contrasting postseason performance captures the unpredicatable nature of the sport of baseball. While the Brewers, leading the National League in regular-season wins, did not advance to the World Series, the Dodgers made it to the finals despite having fewer wins and lacking top-10 players in key statistics. Factors like playoff experience, team depth, balanced contributions across the roster, strategic in-game decisions, and effective bullpen management play pivotal roles in navigating the intricacies and pressures of the sport, which are often not seen in other team sports.


## Data Analysis Capstone Requirements | Spring 2023

**Category 1: Loading Data:**

- Read TWO data files (JSON, CSV, Excel, etc.).

**Category 2: Clean and Operate the Data While Combining Them:**

- Clean your data and perform a pandas merge with your data sets, then calculate some new values based on the new data set.

**Category 3: Visualize/Present Your Data:**

- Make 3 matplotlib or seaborn (or another plotting library) visualizations to display your data.
- *Make a Tableau dashboard to display your data.*

**Category 4: Best Practices:**

- Utilize a virtual environment and include instructions in your README on how the user should set one up.

**Category 5: Interpretation of Your Data:**

- Annotate your code with markdown cells in Jupyter Notebook, write clear code comments, and have a well-written README.md. Tidy up your notebook, and make sure you don't have any empty cells or incomplete cells that don’t do anything. Make sure it’s all functional before your final github commit.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter import messagebox, filedialog, ttk

"""
Une bibliothèque en Python pour le traitement de données tabulaires
"""

class DataProcessor:
    def __init__(self):
        self.data = None

    def load_data_from_csv(self, file_path):
        """Fonction pour le chargement de la donnée

        Args:
            file_path (str): Recupere la donnée via un chemin 
        """
        self.data = pd.read_csv(file_path)

    def calculate_mean(self, column_name):
        """Calcul de la moyenne à travers une colonne choisie

        Args:
            column_name (str): la colonne choisie pour notre calcul

        Returns:
            float: le resultaat de notre calcul
        """
        return self.data[column_name].mean()

    def calculate_median(self, column_name):
        """Calcul de la médiane à travers une colonne choisie

        Args:
            column_name (str): la colonne choisie pour notre calcul

        Returns:
            float: le resultaat de notre calcul
        """
        return self.data[column_name].median()

    def calculate_std_dev(self, column_name):
        """Calcul de l'écart-type à travers une colonne choisie

        Args:
            column_name (str): la colonne choisie pour notre calcul

        Returns:
            float: le resultaat de notre calcul
        """
        return self.data[column_name].std()

    def generate_histogram(self, column_name):
        """Affichaage un histogramme à travers une colonne choisie

        Args:
            column_name (str): la colonne choisie pour notre histogramme
        """
        plt.hist(self.data[column_name])
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.title('Histogram of {}'.format(column_name))
        plt.show()

    def generate_bar_chart(self, x_column, y_column):
        """Affichage d'un diagramme en barre à travers deux colonnes choisies

        Args:
            x_column (str): notre première colonne pour l'axe des abscisses
            y_column (str): notre deuxième colonne pour l'axe des ordonnées
        """
        sns.barplot(x=x_column, y=y_column, data=self.data)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title('Bar Chart: {} vs {}'.format(x_column, y_column))
        plt.show()
    
class DataProcessorGUI:
    def __init__(self, root):
        self.processor = DataProcessor()
        self.root = root
        self.root.title("Data Processor")
        self.root.geometry("300x200")

        self.load_button = Button(root, text="Load CSV", command=self.load_csv)
        self.load_button.pack()

        self.show_button = Button(root, text="Show Data", command=self.display_dataset)
        self.show_button.pack()

        self.mean_button = Button(root, text="Calculate Mean", command=self.calculate_mean)
        self.mean_button.pack()

        self.median_button = Button(root, text="Calculate Median", command=self.calculate_median)
        self.median_button.pack()

        self.std_dev_button = Button(root, text="Calculate Std Dev", command=self.calculate_std_dev)
        self.std_dev_button.pack()

        self.histogram_button = Button(root, text="Generate Histogram", command=self.generate_histogram)
        self.histogram_button.pack()

        self.bar_chart_button = Button(root, text="Generate Bar Chart", command=self.generate_bar_chart)
        self.bar_chart_button.pack()

    def load_csv(self):
        """Affichage d'une fenêtre pour choisir la donnée (csv)
        """
        file_path = filedialog.askopenfilename()
        if file_path:
            self.processor.load_data_from_csv(file_path)
            messagebox.showinfo(title="File Loading",message="CSV loaded successfully.")

    def calculate_mean(self):
        """Affichage de la valeur de la moyenne sur une fenêtre
        """
        column_name = self.ask_columns()
        if column_name:
            messagebox.showinfo(title="Mean", message=self.processor.calculate_mean(column_name))

    def calculate_median(self):
        """Affichage de la valeur de la médiane sur une fenêtre
        """
        column_name = self.ask_columns()
        if column_name:
            messagebox.showinfo(title="Median", message=self.processor.calculate_median(column_name))

    def calculate_std_dev(self):
        """Affichage de la valeur de l'écart-type sur une fenêtre
        """
        column_name = self.ask_columns()
        if column_name:
            messagebox.showinfo(title="Standard Deviation",message=self.processor.calculate_std_dev(column_name))

    def generate_histogram(self):
        """Affichage de notre le histogramme sur une fenêtre
        """
        column_name = self.ask_columns()
        if column_name:
            self.processor.generate_histogram(column_name)

    def generate_bar_chart(self):
        """Affichage de notre diagramme en barre sur une fenêtre
        """
        x_column = self.ask_columns()
        y_column = self.ask_columns()
        if x_column and y_column:
            self.processor.generate_bar_chart(x_column, y_column)
    
    def ask_columns(self):
        """Affichage d'une fenêtre permettant le choix des colonnes
        """
        def on_okay():
            """Permet de quitter la fenêtre après choix de la colonne
            """
            selected_column = column_name_combobox.get()
            if selected_column:
                nonlocal result_column
                result_column = selected_column.strip()
                window.destroy()

        result_column = None
        
        window = Toplevel(self.root)
        window.title("Select Column")

        column_name_combobox = ttk.Combobox(window, values=[i for i in self.processor.data.columns], width=20)
        column_name_combobox.pack(padx=10, pady=10)

        okay_button = Button(window, text="Okay", command=on_okay)
        okay_button.pack(padx=10, pady=5)

        window.wait_window(window)  
        return result_column
    
    def display_dataset(self):
        """Permet d'afficher notre dataset chargée au préalable
        """
        def on_close():
            """Ferme la fenêtre de l'affichage du dataset
            """
            window.destroy()

        window = Toplevel()
        window.title("Data Viewer")

        tree = ttk.Treeview(window)
        tree["columns"] = tuple(self.processor.data.columns)

        for col in self.processor.data.columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)

        for index, row in self.processor.data.iterrows():
            tree.insert("", "end", values=tuple(row))

        tree.pack(expand=YES, fill=BOTH)

        close_button = Button(window, text="Close", command=on_close)
        close_button.pack(pady=10)

        window.mainloop()
    
if __name__ == "__main__":
    root = Tk()
    app = DataProcessorGUI(root)
    root.mainloop()
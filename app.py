import streamlit as st
import pandas as pd

def calculate_dupont(df):
    # Calculating the required financial metrics
    df['Margen Neto (%)'] = (df['Utilidad Neta'] / df['Ventas Netas']) * 100
    df['Rotación (veces)'] = df['Ventas Netas'] / df['Activos Totales']
    df['Apalancamiento (veces)'] = df['Activos Totales'] / df['Capital Contable']
    df['ROE (%)'] = df['Margen Neto (%)'] * df['Rotación (veces)']
    df['ROA (%)'] = df['Rotación (veces)'] * df['Apalancamiento (veces)']
    df['Pay Back Capital (veces)'] = 1 / (df['ROE (%)'] / 100)
    df['Pay Back Activos (veces)'] = 1 / (df['ROA (%)'] / 100)
    return df

def main():
    st.title("Modelo Dupont para Rentabilidad de Negocios")

    # File uploader to upload Excel data
    file = st.file_uploader("Sube el archivo de Excel con los datos.", type=["xlsx"])

    if file:
        # Read the Excel file
        df = pd.read_excel(file)

        # Validate required columns
        required_columns = ['Ventas Netas', 'Utilidad Neta', 'Activos Totales', 'Capital Contable']
        if all(col in df.columns for col in required_columns):
            # Calculate Dupont analysis
            df_result = calculate_dupont(df)

            # Display results
            st.subheader("Reporte Dupont")
            st.dataframe(df_result)
        else:
            st.error(f"El archivo debe contener las siguientes columnas: {', '.join(required_columns)}")

if __name__ == "__main__":
    main()

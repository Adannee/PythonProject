import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide", page_title="EtherScan Wallet Dashboard")


st.sidebar.title("Upload CSV")
uploaded_file = st.sidebar.file_uploader("/Users/ivyadiele/Desktop/PythonProject/EtherscanScraper/data/etherscan_transactions.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date

  
    st.sidebar.title("Filters")
    date_range = st.sidebar.date_input("Select date range", [df["date"].min(), df["date"].max()])
    show_failed = st.sidebar.checkbox("Include failed transactions", value=False)

   
    df_filtered = df[(df["date"] >= date_range[0]) & (df["date"] <= date_range[1])]
    if not show_failed:
        df_filtered = df_filtered[df_filtered["success"] == True]


    st.title("EtherScan Wallet Transaction Dashboard")
    st.markdown(f"Transactions from **{df['from'].iloc[0]}** to {df_filtered['to'].nunique()} addresses")

  
    col1, col2, col3 = st.columns(3)
    col1.metric("Total ETH Sent", f"{df_filtered['value (ETH)'].sum():.4f} ETH")
    col2.metric("Total Tx Fees", f"{df_filtered['tx fee (ETH)'].sum():.4f} ETH")
    col3.metric("Transactions", f"{len(df_filtered)}")

    
    st.subheader("💸 Transaction Fees Over Time")
    fig1, ax1 = plt.subplots(figsize=(10,4))
    sns.lineplot(data=df_filtered, x="timestamp", y="tx fee (ETH)", ax=ax1)
    ax1.set_title("Transaction Fee (ETH) Over Time")
    ax1.tick_params(axis='x', rotation=45)
    st.pyplot(fig1)

    
    st.subheader("📆 ETH Sent Per Day")
    eth_daily = df_filtered.groupby("date")["value (ETH)"].sum().reset_index()
    fig2, ax2 = plt.subplots(figsize=(10,4))
    sns.barplot(data=eth_daily, x="date", y="value (ETH)", ax=ax2)
    ax2.tick_params(axis='x', rotation=45)
    st.pyplot(fig2)

    
    st.subheader("⛽ Gas Used Distribution")
    fig3, ax3 = plt.subplots(figsize=(10,4))
    sns.histplot(df_filtered["gas used"], bins=30, ax=ax3, kde=True)
    st.pyplot(fig3)

    
    st.subheader("✅ Transaction Success Rate")
    fig4, ax4 = plt.subplots()
    df_filtered["success"].value_counts().plot.pie(
        labels=["Success", "Failed"],
        autopct="%1.1f%%",
        startangle=90,
        colors=["#4CAF50", "#FF5722"],
        ax=ax4
    )
    ax4.set_ylabel("")
    st.pyplot(fig4)

else:
    st.info("Upload a CSV file to begin.")
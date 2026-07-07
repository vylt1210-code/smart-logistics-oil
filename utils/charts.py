import plotly.express as px

def line_chart(df, x, y, title):
    fig = px.line(df, x=x, y=y, markers=True, title=title)
    fig.update_layout(template="plotly_white", height=440, margin=dict(l=20,r=20,t=60,b=20))
    return fig

def corr_heatmap(corr):
    fig = px.imshow(corr, text_auto=True, color_continuous_scale="Blues", title="Ma trận tương quan")
    fig.update_layout(template="plotly_white", height=520)
    return fig

def residual_chart(df):
    fig = px.scatter(df, x="OLS_Du_Bao", y="Sai_Lech", title="Residual Plot")
    fig.add_hline(y=0, line_dash="dash")
    fig.update_layout(template="plotly_white", height=440)
    return fig

def bar_chart(df, x, y, title):
    fig = px.bar(df, x=x, y=y, title=title)
    fig.update_layout(template="plotly_white", height=440)
    return fig

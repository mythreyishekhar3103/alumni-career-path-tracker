import pandas as pd
import plotly.graph_objects as go


def create_sankey_from_dataframe(
        df,
        source_column,
        target_column,
        title="Career Path Flow"
):
    """
    Create Sankey Diagram from two columns
    """

    sankey_df = (
        df.groupby(
            [source_column, target_column]
        )
        .size()
        .reset_index(name="count")
    )

    labels = list(
        pd.concat([
            sankey_df[source_column],
            sankey_df[target_column]
        ]).unique()
    )

    label_to_index = {
        label: idx
        for idx, label in enumerate(labels)
    }

    source = [
        label_to_index[val]
        for val in sankey_df[source_column]
    ]

    target = [
        label_to_index[val]
        for val in sankey_df[target_column]
    ]

    value = sankey_df["count"]

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(
                        color="black",
                        width=0.5
                    ),
                    label=labels
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value
                )
            )
        ]
    )

    fig.update_layout(
        title_text=title,
        font_size=12
    )

    return fig


def create_custom_sankey(
        labels,
        source,
        target,
        value,
        title="Career Flow"
):
    """
    Create custom Sankey diagram
    """

    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    label=labels
                ),
                link=dict(
                    source=source,
                    target=target,
                    value=value
                )
            )
        ]
    )

    fig.update_layout(
        title_text=title,
        font_size=12
    )

    return fig

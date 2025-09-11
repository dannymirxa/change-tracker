from collections import defaultdict
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import textwrap

def dict_to_nested_dict(data: dict) -> dict:
    denormalized_drivers_question_data = defaultdict(list)

    for driver, question, answer in data:
        denormalized_drivers_question_data[driver].append({
            "question": question,
            "answer": answer
        })
    denormalized_drivers_question_data = dict(denormalized_drivers_question_data)
    return denormalized_drivers_question_data

def nest_by_drivers_name(data: dict) -> dict:
    denormalized_drivers_question_data = defaultdict(list)

    for cycle, drivers_name, answer in data:
        denormalized_drivers_question_data[drivers_name].append({
            "cycle": cycle,
            "answer": answer
        })
    denormalized_drivers_question_data = dict(denormalized_drivers_question_data)
    return denormalized_drivers_question_data

def nest_by_qcode(data: dict) -> dict:
    denormalized_drivers_question_data = defaultdict(list)

    for cycle, qcode, answer in data:
        denormalized_drivers_question_data[qcode].append({
            "cycle": cycle,
            "answer": answer
        })
    denormalized_drivers_question_data = dict(denormalized_drivers_question_data)
    return denormalized_drivers_question_data

def list_to_dict(data: list) -> dict:
    data_dict = {row['question']: row['answer'] for row in data}
    return data_dict


def figure_scale_by_value(
    title: str,
    data: dict,
    wrap_width: int = 30,
    bargap: float = 0.8,
    bar_thickness: float = 0.1,
    left_margin: int = 220
):
    """
    Build a horizontal bar chart with wrapped y-axis labels and adjustable spacing.

    Args:
        title: Figure title.
        data: Dict[str, float] mapping Metric -> Score.
        wrap_width: Characters per line for y-axis label wrapping (uses word boundaries).
        bargap: Space between bars of different categories (0=no gap, 1=max gap).
        bar_thickness: Relative thickness of each bar within its category band (0..1).
        left_margin: Left margin in px to prevent clipping of long wrapped labels.
    """
    # Convert to DataFrame
    df = pd.DataFrame({
        "Metric": list(dict(data).keys()),
        "Score": list(dict(data).values())
    })

    # Base bar chart
    fig = px.bar(
        df,
        x="Score",
        y="Metric",
        orientation="h",
        title=title
    )

    # Layout sizing (height scales with number of bars)
    bar_px = 50
    top_bottom_margin = 130
    n = len(df["Metric"])
    fig.update_layout(
        minreducedheight = 400,
        height=top_bottom_margin + bar_px * n,
        bargap=bargap,            # controls distance between categories
        margin=dict(l=left_margin)
    )

    # Make bars thinner/thicker (relative to the category band)
    fig.update_traces(width=bar_thickness, selector=dict(type="bar"))

    # Overlay marker trace (unchanged)
    fig.add_trace(
        go.Scatter(
            x=df["Score"],
            y=df["Metric"],
            mode="markers",
            marker=dict(symbol="circle", size=10, color="rgba(0,0,0,1)"),
            showlegend=False,
            # hoverinfo="skip"
        )
    )

    # X-axis range
    fig.update_xaxes(range=[1, 7])

    # Wrap y-axis tick labels using <br>
    def wrap_label(s: str, width: int = 30) -> str:
        return "<br>".join(textwrap.wrap(s, width=width)) if isinstance(s, str) else s

    wrapped_ticktext = [wrap_label(m, width=wrap_width) for m in df["Metric"]]
    fig.update_yaxes(
        tickmode="array",
        tickvals=df["Metric"],
        ticktext=wrapped_ticktext,
        automargin=True,
        categoryorder="array",            # keep original order
        categoryarray=list(df["Metric"])
    )

    return fig

def figure_scale_by_percentage(
    title: str,
    data: dict,
    wrap_width: int = 30,
    bargap: float = 0.8,
    bar_thickness: float = 0.1,
    left_margin: int = 220
):
    """
    Build a horizontal bar chart with wrapped y-axis labels and adjustable spacing.

    Args:
        title: Figure title.
        data: Dict[str, float] mapping Metric -> Score.
        wrap_width: Characters per line for y-axis label wrapping (uses word boundaries).
        bargap: Space between bars of different categories (0=no gap, 1=max gap).
        bar_thickness: Relative thickness of each bar within its category band (0..1).
        left_margin: Left margin in px to prevent clipping of long wrapped labels.
    """
    # Convert to DataFrame
    df = pd.DataFrame({
        "Metric": list(dict(data).keys()),
        "Score": list(dict(data).values())
    })

    # Base bar chart
    fig = px.bar(
        df,
        x="Score",
        y="Metric",
        orientation="h",
        title=title
    )

    # Layout sizing (height scales with number of bars)
    bar_px = 50
    top_bottom_margin = 130
    n = len(df["Metric"])
    fig.update_layout(
        minreducedheight = 400,
        height=top_bottom_margin + bar_px * n,
        bargap=bargap,            # controls distance between categories
        margin=dict(l=left_margin)
    )

    # Make bars thinner/thicker (relative to the category band)
    fig.update_traces(width=bar_thickness, selector=dict(type="bar"))

    # Overlay marker trace (unchanged)
    fig.add_trace(
        go.Scatter(
            x=df["Score"],
            y=df["Metric"],
            mode="markers",
            marker=dict(symbol="circle", size=10, color="rgba(0,0,0,1)"),
            showlegend=False,
            # hoverinfo="skip"
        )
    )

    # X-axis range
    fig.update_xaxes(range=[0, 100])

    # Wrap y-axis tick labels using <br>
    def wrap_label(s: str, width: int = 30) -> str:
        return "<br>".join(textwrap.wrap(s, width=width)) if isinstance(s, str) else s

    wrapped_ticktext = [wrap_label(m, width=wrap_width) for m in df["Metric"]]
    fig.update_yaxes(
        tickmode="array",
        tickvals=df["Metric"],
        ticktext=wrapped_ticktext,
        automargin=True,
        categoryorder="array",            # keep original order
        categoryarray=list(df["Metric"])
    )
    
    return fig

def figure_line_by_cycle(
    title: str,
    data: list,
    wrap_width: int = 30,
    left_margin: int = 80,
    marker_size: int = 8,
    line_width: int = 2
):
    """
    Build a line chart where Y axis is 'cycle' and X axis is 'answer'.

    Args:
        title: Figure title.
        data: List[dict] with items like {'cycle': int, 'answer': number}.
        wrap_width: Characters per line for y-axis label wrapping (used if cycles are strings).
        left_margin: Left margin in px to prevent clipping of y-axis labels.
        marker_size: Size of the markers on the line.
        line_width: Width of the connecting line.
    """
    # Normalize input list of dicts to DataFrame
    df = pd.DataFrame(data)

    # Ensure expected columns exist
    if "cycle" not in df.columns or "answer" not in df.columns:
        raise ValueError("data must be a list of dicts containing 'cycle' and 'answer' keys")

    # Sort by cycle to ensure line order
    try:
        df = df.sort_values("cycle")
    except Exception:
        # If cycles are non-sortable, keep original order
        pass

    # Build line chart: X = answer, Y = cycle
    fig = px.line(
        df,
        x="answer",
        y="cycle",
        title=title,
        markers=True
    )

    # Update marker and line appearance
    fig.update_traces(marker=dict(size=marker_size), selector=dict(mode="markers"))
    fig.update_traces(line=dict(width=line_width), selector=dict(mode="lines"))

    # Layout sizing (height scales with number of unique cycles)
    # Increased defaults to provide taller charts per user request
    bar_px = 70
    top_bottom_margin = 200
    n = df["cycle"].nunique()
    fig.update_layout(
        minreducedheight=400,
        height=top_bottom_margin + bar_px * max(1, n),
        margin=dict(l=left_margin)
    )

    # If cycles are strings (long labels) wrap them
    def wrap_label(s: str, width: int = 30) -> str:
        return "<br>".join(textwrap.wrap(str(s), width=width)) if isinstance(s, (str, int)) else s

    # Prepare tick labels for y axis (preserve original ordering)
    cycle_vals = list(dict.fromkeys(df["cycle"].tolist()))
    wrapped_ticktext = [wrap_label(m, width=wrap_width) for m in cycle_vals]
    fig.update_yaxes(
        tickmode="array",
        tickvals=cycle_vals,
        ticktext=wrapped_ticktext,
        automargin=True,
        categoryorder="array",
        categoryarray=cycle_vals
    )

    # Provide some padding on x axis depending on data range
    try:
        xmin = float(df["answer"].min())
        xmax = float(df["answer"].max())
        span = xmax - xmin
        pad = max(0.1 * span, 1) if span != 0 else 1
        fig.update_xaxes(range=[xmin - pad, xmax + pad])
    except Exception:
        # If conversion fails, leave axis autoscaling
        pass

    return fig

from agents.monitor import monitor

def test_render_summary_runs():
    s = monitor.render_summary()
    assert "# Monitor A" in s

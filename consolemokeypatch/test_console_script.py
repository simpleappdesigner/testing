def test_stdin(script_runner, monkeypatch):
    import io
    monkeypatch.setattr('sys.stdin', io.StringIO('[{"k": ["1", "2"]}]'))
    ret = script_runner.run("test_console_script.py", "-", print_result=True)
    assert ret.success
    print(ret.print())
    assert "k" in ret.stdout
    #assert ret.stderr == ""
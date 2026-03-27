def format_output(tc):
    if tc["status"] == "SKIPPED":
        return f'{tc["id"]} | Module: {tc["module"]} | Priority: {tc["priority"]} → SKIPPED'
    else:
        return f'{tc["id"]} | Module: {tc["module"]} | Priority: {tc["priority"]} | Expected: {tc["expected"]} | Actual: {tc["actual"]} → {tc["status"]}'
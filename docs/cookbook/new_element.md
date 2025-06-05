# Adding a New CIM Element

This quick guide shows how to extend **cgmes-py** with a new CIM element. The steps mirror the existing workflow used in the tests.

1. **Regenerate models**

   ```bash
   python generate_cgmes_project.py
   ```

2. **Create or update dataclasses**

   Edit the generated model to add the new element with appropriate `xpath` metadata.

3. **Write a test**

   Add a test under `tests/` ensuring the element can be parsed and written back without loss.


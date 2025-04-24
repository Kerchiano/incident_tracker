Input commands in Command Prompt(cmd) Windows.
1.  Create a working directory:
    ```bash
    mkdir test-directory
    ```
    ```bash
    cd test-directory
    ```
2. Clone the repository:
    ```bash
    git clone https://github.com/Kerchiano/incident_tracker.git
    ```

3. After cloning, navigate to `C:\...\test-directory\incident_tracker`:

    ```bash
    cd incident_tracker
    ```

4. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

5. Activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```

6. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

7. Create the `.env` file:

    ```bash
    echo. > .env
    ```

8. Congratulations! Open your browser and go to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) to check the API endpoints.

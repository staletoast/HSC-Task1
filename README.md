> [!Caution]
>
> # DISCLAIMER
>
> **This progressive web app has been designed with a range of security vulnerabilities. The app has been specifically designed for students studying the [NESA HSC Software Engineering Course](https://curriculum.nsw.edu.au/learning-areas/tas/software-engineering-11-12-2022/content/n12/fa039e749d). The app is NOT secure and should only be used in a sandbox environment.**

## Sandbox Environments

Sandboxing creates a safe place to install or execute a program, particularly a suspicious one, without exposing the rest of your system or network. It keeps the code contained in a test environment, so it can't change the state of the host machine, operating system or networked resources. Simple-to-use sandbox environments for Python Flask are listed below, and the UI should be accessed from the latest version of a secure browser such as Chromium or Edge.

- [GitHub Codespaces](https://github.com/features/codespace)
- [CodeSandbox.io](https://codesandbox.io/)\*
- [Docker Container](https://code.visualstudio.com/docs/devcontainers/containers)\*

\* Requires further configuration

> [!Important] > **The Unsecure PWA includes the [.codesandbox](.codesandbox), [.devcontainer](.devcontainer) and [.vscode](.vscode) to auto-configure all the above sandboxes.**

Other Sandbox options:

- Virtual machine
- Ubuntu on a USB or in a virtual machine
- Qubes OS in a virtual machine

---

## Dependencies & Deployment

### Dependencies

1. [VSCode](https://code.visualstudio.com/download)
2. [Python 3.x](https://www.python.org/downloads/)
3. [GIT 2.x.x +](https://git-scm.com/downloads)
4. Flask: `pip install flask`
5. The resources and samples in [.student_resources](.student_resources/) require additional dependencies. Please refer to the README.md in each folder.

> [!Important]
> MacOS users may have a `pip3` soft link instead of `pip`, run the below commands to see what path your system is configured with and use that command through the project.
>
> ```bash
> pip show pip
> pip3 show pip
> ```

### Deployment

```bash
python main.py
```

Once deployed, the app can be accessed on either:

- [http://localhost:5000](http://localhost:5000)
- [http://127.0.0.1:5000](http://127.0.0.1:5000)
- [http://{10.185.x.x}:5000](http://10.185.0.0:5000) where 10.185.x.x is the LAN IP address for the host

> [!Tip]
> Many of the resources in [.student_resources](.student_resources/) have been written assuming the student is running the app locally, so http://127.0.0.1:5000 has been used. If the teacher is hosting the app and students are black-box testing, then the HTML/JS in the examples will need changing to reference the remote URL.

---

## Working Log-In
Username : Developer
Password : Password

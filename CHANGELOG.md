commit 7d9dcc7f31426dc16be2c3c6963d23269ffcccfb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 23 21:39:00 2021 -0400

    Updated default GitHub actions workflows
    
    - Leverage cache
    - Add pre-commit
    - Closes #13

commit 415972af293effdf66cd02353e1c3644e886848a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 23 21:11:16 2021 -0400

    Added Probot configs, etc.
    
    - Closes #11

commit e51f93a360730719fbb798d8276eb4f7a7acdc4c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 31 22:29:52 2021 -0400

    Added user's home/.ssh mount
    
    - This adds the user's home/.ssh directory as a volume mount in read
      only
    - Because the user's .gitconfig is copied into the running dev
      container, certain configuration options for git repos can be
      impacted. This will in most cases keep the user from having to manually
      configure the .gitconfig in the container.
    - Example is that if using ssh repos, the user's ssh keys may be
      required anyways

commit c785ecbda1a173aa1df6281d35eba0e3b1384b11
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 31 14:38:31 2021 -0400

    Downgraded Python default version for devcontainer
    
    Forgot to change to Python 3.7.10 as default
    
    PyATS fails on Python > 3.8.x

commit ce49171f9f4404af4f34a34a409c51ec1a5f03e3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 31 11:27:28 2021 -0400

    Updated Python requirements, etc.
    
    - pyats requires <=3.8 currently. Changed to 3.7.x
    - Added robotframework for testing
    - exported requirements w/out hashes
      - Hashes causing issues w/pip radmomly

commit 0618e29f6786138ae1c094bdc2cc0af347409696
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 29 16:03:07 2021 -0400

    Added Python virtual envs to ignore

commit f235a11e5b225f4c0e25ea60a8798bac43feb088
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 29 12:18:57 2021 -0400

    First commit of devcontainer
    
    This is at least a start for VSCode dev container usage

commit fd59e5134d9d6cb5e61d107bbd5ef020ca86fefa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 29 09:43:39 2021 -0400

    First commit for Poetry and validation testing
    
    Added Poetry functionality
    
    Added GitHub actions testing for cookiecutter

commit 9f2ce9b3f4114b0dd45af0a36748681395a6f986
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 29 10:41:08 2021 -0400

    Updated repo usage
    
    Updated example project creation to show usage

commit c009e80896cc20afebd0c3de836931ab9242b11c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 1 11:31:47 2020 -0400

    Added checkout step to latest to leverage submodules

commit d02e28615410ef5f1feb0ac13fe7d2d14f138774
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Aug 10 13:38:18 2020 -0400

    Added Flake8 config
    
    - The only thing we have added so far is to exlude venv/ directory

commit 8bf1d6fa60cbcb20b7223e8b4a3d97b89ef3e1d5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu May 14 20:44:18 2020 -0400

    Switching to pip-tools to manage Python reqs

commit a5db1778ea5234b1f6c17c12e0e985ea483532c1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 25 01:39:24 2020 -0400

    Added logging rotation
    
    This change implements logging rotation by default to ensure that any
    logging for a project rotates at midnight. This will help minimize the
    sizes of log files.

commit ff85b422069f54b36141ab728b0efcd747e4ea05
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 22 14:30:45 2020 -0400

    Fixed title page for README

commit dac8427bdd964d51e54e554336f2348de875eb07
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 09:47:05 2020 -0400

    Fixed formatting issue

commit 6afd1024bf9e684e2a1a101b799ae2e1caeaf7dc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 21 09:17:58 2020 -0400

    Added mkdocs to template

commit ba96f8240c9809d4ee3f856ebd3e2271bfcc89a8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 17:18:02 2020 -0400

    Updated module docstring formatting

commit c2dcfefdac90a332da7630a7e69757e16e06a978
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 16:49:39 2020 -0400

    Added logs/ to gitignore

commit 092709ab6ea8dd4d862aab2aa83dbdf8b19570ca
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 16:41:37 2020 -0400

    New updated constructs based on my best practices and testing

commit 924d989c579b8dea9c4bc4e6dd6234b3f482e48b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Mar 18 16:33:31 2020 -0400

    Changed top level parent directory
    
    This allows the parent directory to be named different than what the
    module name is. If needed.

commit 6b8ab3ab37de8feeb79f7f03a74e2b41e261ac42
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 13 20:19:33 2020 -0400

    Renamed main directory to be independent of project_slug

commit 65b0a9d363a2d95725bd84fcaaa7d98f58522496
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 9 22:52:44 2020 -0400

    Enhancement: Cleaned up CI tests, etc.

commit 4b5723f7986969831d08463d89397fc9adde1f95
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 1 00:56:23 2020 -0500

    Updated changelog

commit 51e2ceaef61a55e9f9a610d1dab01c527844b5e6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 1 00:56:14 2020 -0500

    Updated Python development requirements

commit 3cd3d4e4281da24402cab3568801436a21928ee7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 1 00:55:54 2020 -0500

    Added VSCode dir to ignore

commit 7f63a96fc4269d4c14e20a71507182500d145a50
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Mar 1 00:55:34 2020 -0500

    Updated CI linting configs
    
    - They were wrong and not correct for Python projects

commit f9dbef6c52a731451316cc230e127435b297bd94
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 28 00:54:33 2020 -0500

    Create LICENSE.md

commit 9b01a48ab8e2cc5a20af700afb49c9df5b26ff03
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 28 00:54:01 2020 -0500

    Create CODE_OF_CONDUCT.md

commit 67c88029a7d6ce83d0656936932464bb629fa5c5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 28 00:49:42 2020 -0500

    first commit

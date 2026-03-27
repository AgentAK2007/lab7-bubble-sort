# Project Journal - lab7-bubble-sort

### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 00:00
- **User**: default_user
- **Prompt**: Create a local git repo for this project
- **CoPilot Mode**: Edit
- **CoPilot Model**: Claude Haiku 4.5
- **Socratic Mode**: ON
- **Changes Made**: Initialized git repository with `git init`
- **Context and Reasons for Changes**: Project now has version control enabled. The `.github/` folder structure and journal-logger agent are in place to support comprehensive tracking of development activities.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 10:33
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you help me learn by writing a skeleton bubble sort app with stubs functions, with comments and TODOs that will indicate what I need to do?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Added a Bubble Sort skeleton app with stub functions, comments, and numbered TODOs in main.py.
- **Context and Reasons for Changes**: User requested a guided learning scaffold instead of a full implementation, so the file now provides structured steps for incremental coding practice.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 11:36
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you set up testing for this app, using basic pytest features and create 5 tests?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Added pytest-based test_main.py with 5 tests and installed pytest in the project virtual environment.
- **Context and Reasons for Changes**: User requested a basic pytest setup and five tests; test execution now works and currently reports failing tests due TODO stubs remaining in main.py.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 11:47
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you create or update README.md for this project?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Created README.md with project overview, file map, requirements, run instructions, test instructions, and Bubble Sort complexity notes.
- **Context and Reasons for Changes**: User asked for a project README, so documentation was added for easier onboarding and execution.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:01
- **User**: arkar.thurein@epita.fr
- **Prompt**: I am interested in the In-place redraw option. Help me implement this. Create the stubs and todos in main.py.
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Added in-place animation scaffolding in main.py with redraw helpers, ASCII bar rendering, comparison-by-comparison visual sort path, and TODOs for student-driven improvements.
- **Context and Reasons for Changes**: User requested an in-place redraw terminal approach with stubs and TODO guidance rather than a fully polished visualization framework.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:12
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you finish implementing the stub functions?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: ON
- **Changes Made**: Finalized visualization implementation details in main.py by improving in-place redraw behavior, handling empty/single-element visual runs safely, validating negative delay input, and polishing summary output.
- **Context and Reasons for Changes**: User requested completion of stubs; file logic was mostly implemented, so remaining stub-level rough edges were completed for reliability and smoother animation behavior.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:14
- **User**: arkar.thurein@epita.fr
- **Prompt**: Turn Socratic mode off for this request, and do finish implementing the terminal
visualization feature.
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: OFF
- **Changes Made**: Completed terminal visualization implementation with dynamic bar sizing from terminal width, robust clear/redraw fallback behavior, and clearer per-frame action labeling while preserving comparison-by-comparison animation.
- **Context and Reasons for Changes**: User requested non-Socratic direct implementation and completion of in-place terminal visualization functionality.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:16
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you clean up the code and update the documentation ?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: OFF
- **Changes Made**: Cleaned up main.py with constants, reduced duplication via helper function for max scaling, improved empty-input validation and delay handling messages, and updated README.md to document visualization mode and runtime behavior.
- **Context and Reasons for Changes**: User requested code cleanup and documentation refresh to better reflect current implementation and usage.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:21
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you implement a Pygame based visualization?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: OFF
- **Changes Made**: Added pygame_visualizer.py with a full 2D Bubble Sort renderer and controls, integrated mode selection in main.py, installed pygame dependency, and updated README.md documentation.
- **Context and Reasons for Changes**: User requested a real 2D graphics rendering approach for Bubble Sort visualization.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:23
- **User**: arkar.thurein@epita.fr
- **Prompt**: Can you install PyGame in the local virtual environment and then create a 'requirements.txt'
that includes the required libraries to run this project, and finally update README to explain all
of this?
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: OFF
- **Changes Made**: Installed pygame and pytest in the local virtual environment, added requirements.txt with project dependencies, and updated README.md with virtual environment setup and pip install -r requirements.txt workflow.
- **Context and Reasons for Changes**: User requested dependency installation plus reproducible setup documentation.
### **New Interaction**
- **Agent Version**: 2.2
- **Date**: 27-03-2026 12:28
- **User**: arkar.thurein@epita.fr
- **Prompt**: "main.py is too big and looks messy. Can you refactor the project and enforce the separation
of concerns between UI and Logic? Use several files if needed.
- **CoPilot Mode**: Edit
- **CoPilot Model**: GPT-5.3-Codex
- **Socratic Mode**: OFF
- **Changes Made**: Refactored project into separate modules for logic and UI by adding sorting_logic.py and terminal_visualizer.py, slimming main.py to an orchestrator, updating pygame_visualizer.py to consume shared logic steps, and updating tests and README accordingly.
- **Context and Reasons for Changes**: User requested stronger separation of concerns and cleaner project structure.

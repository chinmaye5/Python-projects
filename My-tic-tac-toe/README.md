# Tic Tac Toe with Flask

A modern, web-based Tic Tac Toe game built using Flask for the backend and HTML/CSS/JavaScript with Tailwind CSS for the frontend. The game features a clean, responsive UI, real-time move updates, and robust game logic.

## Features
- 3x3 Tic Tac Toe grid with alternating X and O players.
- Displays current player's turn, winner, or draw status.
- Reset button to start a new game.
- Responsive design with hover effects and smooth transitions.
- Backend validation to prevent invalid moves.
- Hosted at: [https://github.com/Pravesh-Sudha/Python-projects.git](https://github.com/Pravesh-Sudha/Python-projects.git)

## Prerequisites
- Python 3.x
- Flask (`pip install flask`)
- A modern web browser

## Project Structure
```
My-tic-tac-toe/
├── app.py
|-- Dockerfile
└── templates/
    └── index.html
```

- `app.py`: Flask backend handling game logic, move processing, and state management.
- `templates/index.html`: Frontend with HTML, Tailwind CSS, and JavaScript for UI and interactivity.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Pravesh-Sudha/Python-projects.git
   cd Python-projects/My-tic-tac-toe
   ```

2. **Install Dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

4. **Access the Game**:
   - Open a browser and navigate to `http://127.0.0.1:5000`.

## How to Play
- Click any cell in the 3x3 grid to place an X or O (players alternate).
- The status bar shows the current player's turn or game outcome (win/draw).
- Click **Reset Game** to clear the board and start a new game.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, JavaScript, Tailwind CSS (via CDN)
- **Game Logic**: Server-side move validation and winner detection

## Screenshots
*(Optional: Add screenshots of the game UI here by updating the README in the repository.)*

## Contributing
Contributions are welcome! Please:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For issues or suggestions, open an issue on the [GitHub repository](https://github.com/Pravesh-Sudha/Python-projects.git) or contact the maintainer.
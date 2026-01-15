# Palo Alto NGFW Exam Simulation (Modern PAN-OS 11.x)

This project provides a comprehensive simulation environment for modern Palo Alto Networks Next-Generation Firewall (NGFW) exams. It is updated for the latest PAN-OS 11.x features.

## Features
- **300 unique questions** curated for the modern NGFW exam environment.
- **5 Organized Groups** of 60 questions each for focused study.
- **Random Mode** to shuffle 60 questions from the entire 300-question database.
- **Marathon Mode** to attempt all 300 questions in one session.
- **Modern Content**: Focus on Advanced Threat Prevention, Cloud Identity Engine, AIOps, SD-WAN, and PAN-OS 11.0 innovations.
- Immediate feedback and detailed explanations for every answer.
- Final scoring and pass/fail result (70% threshold).

## How to Run

### On Computer (Terminal)
1. Ensure you have Python installed.
2. Run the simulation using:
   ```bash
   python main.py
   ```

### On iPad / Mobile / Browser
1. You can now run this as a web application!
2. Simply open `index.html` in any web browser.
3. If you want to use it on your iPad:
   - **Option A: GitHub Pages (Recommended)**
     1. Upload the files to a GitHub repository.
     2. Go to Settings -> Pages.
     3. Select the branch (usually `main`) and folder (`/root`), then click Save.
     4. Wait a minute and your exam will be live at `https://yourusername.github.io/paloexam/`.
   - **Option B: Local Web Server app**
     - Use a "Web Server" app from the App Store to host these files locally.
   - **Option C: Direct Transfer (AirDrop/Files)**
     - Transfer both `index.html` and `questions.json` to your iPad.
     - Open `index.html`. You will see **"iPad / Mobile Instructions"** on the screen.
     - Tap the **"Choose File"** button and select the `questions.json` file you just transferred.
     - The exam menu will appear instantly once the file is selected.
     - **Note**: The app will save the questions on your device, so you only need to select the file once. If you need to refresh the questions, you can clear your browser cache or open the page with `index.html?debug=1`.

## New Features
- **One Question at a Time**: Better focus and clean UI.
- **Immediate Feedback**: See the right answer and explanation instantly if you get it wrong.
- **Review Mode**: All wrong answers are saved and displayed at the end for focused study.
- **70% Passing Score**: Real-time calculation and pass/fail status.

## Exam Modes
1. **Group 1**: Modern Architecture & Security (Questions 1-60)
2. **Group 2**: Advanced Security & Threat Prevention (Questions 61-120)
3. **Group 3**: Identity & Access Management (Questions 121-180)
4. **Group 4**: Network Services (SD-WAN, Routing, NAT) (Questions 181-240)
5. **Group 5**: Operations & Troubleshooting (Questions 241-300)
6. **Random 60**: Randomly pulls 60 questions from the database.
7. **All Questions**: The full 300-question experience.

## Exam Domains Covered
- **Modern Architecture**: Inline Deep Learning, Advanced Threat Prevention, Advanced URL Filtering.
- **Advanced Security**: DNS Security, Advanced WildFire, SaaS Security, IoT Security.
- **Identity & Access**: Cloud Identity Engine (CIE), User-ID, GlobalProtect, HIP Profiles.
- **Network Services**: SD-WAN, NAT (DIPP, Static), Virtual Routers, PBF.
- **Management & Operations**: AIOps for NGFW, Panorama (Device Groups, Templates), Best Practice Assessment (BPA).
- **Decryption**: SSL Forward Proxy, Inbound Inspection, Decryption Broker.
- **High Availability**: Active/Passive, Active/Active, HA Links (HA1, HA2, HA3).

## Adding More Questions
You can add more questions by editing the `questions.json` file. Follow the existing JSON structure:
```json
{
  "id": 21,
  "domain": "Domain Name",
  "question": "Your question text here?",
  "options": {
    "a": "Option A",
    "b": "Option B",
    "c": "Option C",
    "d": "Option D"
  },
  "answer": "a",
  "explanation": "Why this answer is correct."
}
```

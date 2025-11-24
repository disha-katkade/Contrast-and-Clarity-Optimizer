```mermaid
    graph TD;
        A[ Start Webcam Capture] --> B{Read Video Frame };
        B -- Resize Frame (640x480) --> C[ Convert to Grayscale ];
        C -- Contrast Boost --> D[Histogram Equalization ];
        D --> E{ Canny Edge Detection };
        E -- Weighted Addition for Enhancement --> F[Overlay Edges on Original Frame ];
        F --> G[Display Enhanced Output Frame];
        G -- if user presses 's' --> H[Save Frame as Image];
        G -- if user presses 'q' --> I[Quit and Stop System];
        H --> J[Write Frame to Output Video File Automatically];
        I --> J
         

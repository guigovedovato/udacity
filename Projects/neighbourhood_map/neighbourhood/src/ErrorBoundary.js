import React, { Component } from 'react';

class ErrorBoundary extends Component {
    constructor(props) {
      super(props);
      this.state = { hasError: false, errorInfo: null };
    }
  
    static getDerivedStateFromError(error) {
      // Update state so the next render will show the fallback UI.
      return { hasError: true };
    }
  
    componentDidCatch(error, errorInfo) {
      // Log the error to state
      this.setState({
        error: error,
        errorInfo: errorInfo
      })
    }
  
    render() {
        if (this.state.errorInfo) {
          // Error path
          return (
            <div>
              <h2>Something went wrong.</h2>
              <details style={{ whiteSpace: 'pre-wrap' }}>
                {this.state.error && this.state.error.toString()}
                <br />
                {this.state.errorInfo.componentStack}
              </details>
            </div>
          );
        }
        // Normally, just render children
        return this.props.children;
    }  
}

  export default ErrorBoundary
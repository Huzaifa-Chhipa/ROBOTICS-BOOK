import React, { useState, useRef, useEffect } from 'react';
import styles from './styles.module.css';

interface Message {
  id: string;
  text: string;
  isUser: boolean;
  timestamp: Date;
}

const Chatbot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      text: 'Hello! I\'m your AI assistant for the Physical AI & Humanoid Robotics book. How can I help you today?',
      isUser: false,
      timestamp: new Date()
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<null | HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async () => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      text: inputValue,
      isUser: true,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Determine the API URL based on environment
      // If running on localhost, connect to backend at port 8000
      // For production, connect to Hugging Face backend
      const isLocalhost = typeof window !== 'undefined' &&
        (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1');

      let apiUrl;
      if (isLocalhost) {
        // For local development, connect to your backend running on port 7860
        apiUrl = 'https://huzaifachhipa-rag-chatbot.hf.space/api/v1/';
      } else {
        // Production: Use the Hugging Face backend URL
        // Docusaurus processes environment variables at build time
        // The REACT_APP_API_URL will be replaced with the actual value during build
        apiUrl = process.env.REACT_APP_API_URL || 'https://huzaifachhipa-rag-chatbot.hf.space/api/v1/';
      }

      console.log('Attempting to connect to:', apiUrl); // Debug log
      console.log('Current hostname:', typeof window !== 'undefined' ? window.location.hostname : 'N/A'); // Debug log

      const response = await fetch(apiUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: inputValue })
      });

      console.log('Response received:', response.status); // Debug log

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
      }

      const data = await response.json();

      // Validate that we received a proper response
      if (!data || !data.answer) {
        throw new Error('Invalid response format from server');
      }

      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: data.answer,
        isUser: false,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);

      let errorMessageText = 'Sorry, I encountered an error. Please try again.';

      // Provide more specific error messages based on the error type
      if (error instanceof TypeError) {
        // This usually indicates a network error or CORS issue
        if (error.message.includes('fetch')) {
          errorMessageText = 'Network error: Unable to connect to the chatbot service. This could be due to CORS restrictions or the backend server being unavailable.';
        } else {
          errorMessageText = `Network error: ${error.message}`;
        }
      } else if (error instanceof Error) {
        if (error.message.includes('404')) {
          errorMessageText = 'Chatbot API endpoint not found. Please check if the backend is properly configured.';
        } else if (error.message.includes('500')) {
          errorMessageText = 'The chatbot service encountered an internal error. Please try again later.';
        } else if (error.message.includes('401') || error.message.includes('403')) {
          errorMessageText = 'Access denied. Please check if the API keys are properly configured.';
        } else {
          errorMessageText = `Error: ${error.message}`;
        }
      } else {
        errorMessageText = 'An unknown error occurred. Please try again.';
      }

      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        text: errorMessageText,
        isUser: false,
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  return (
    <div className={styles.chatbotContainer}>
      <button
        className={styles.chatbotButton}
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Open chatbot"
      >
        <img src="/img/robot.png" alt="Chatbot" />
      </button>

      {isOpen && (
        <div className={`${styles.chatbotWindow} ${isOpen ? styles.open : ''}`}>
          <div className={styles.chatbotHeader}>
            <img src="/img/robot.png" alt="AI Assistant" />
            <span>AI Robotics Assistant</span>
          </div>

          <div className={styles.chatMessages}>
            {messages.map((message) => (
              <div
                key={message.id}
                className={`${styles.message} ${message.isUser ? styles.userMessage : styles.botMessage}`}
              >
                {!message.isUser && (
                  <img src="/img/robot.png" alt="Bot" />
                )}
                {message.text}
              </div>
            ))}

            {isLoading && (
              <div className={styles.typingIndicator}>
                <span className={styles.typingDot}></span>
                <span className={styles.typingDot}></span>
                <span className={styles.typingDot}></span>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className={styles.chatInputContainer}>
            <input
              type="text"
              className={styles.chatInput}
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask about robotics..."
              disabled={isLoading}
            />
            <button
              className={styles.sendButton}
              onClick={sendMessage}
              disabled={isLoading}
              aria-label="Send message"
            >
              <img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'%3E%3Cpath d='M3 20v-6l14-1.5v-5L3 9v-6l18 9-18 9z'/%3E%3C/svg%3E" alt="Send" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Chatbot;
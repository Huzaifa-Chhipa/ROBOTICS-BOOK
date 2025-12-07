import React from 'react';
import { useLocation } from '@docusaurus/router';

function CurrentLocation(): JSX.Element {
  const location = useLocation();
  const pathParts = location.pathname.split('/').filter(Boolean);

  // Simple display for current location, can be enhanced later
  return (
    <div style={{ padding: '10px', backgroundColor: '#f0f0f0', borderRadius: '5px', margin: '10px 0' }}>
      You are currently at: <strong>/{pathParts.join('/')}</strong>
    </div>
  );
}

export default CurrentLocation;

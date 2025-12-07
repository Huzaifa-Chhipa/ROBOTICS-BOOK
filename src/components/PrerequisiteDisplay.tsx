import React from 'react';
import Link from '@docusaurus/Link'; // Docusaurus Link component

interface PrerequisiteDisplayProps {
  prerequisites: string[]; // List of chapter slugs that are prerequisites
}

function PrerequisiteDisplay({ prerequisites }: PrerequisiteDisplayProps): JSX.Element | null {
  if (!prerequisites || prerequisites.length === 0) {
    return null; // Don't render if there are no prerequisites
  }

  return (
    <div style={{
      borderLeft: '4px solid #3073D4',
      padding: '10px 15px',
      margin: '20px 0',
      backgroundColor: '#e6f0fa',
      borderRadius: '4px'
    }}>
      <p style={{ fontWeight: 'bold', marginBottom: '5px' }}>Prerequisites:</p>
      <ul>
        {prerequisites.map((slug, index) => (
          <li key={index}>
            <Link to={`../${slug}`}>{slug}</Link> {/* Assumes relative path */}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PrerequisiteDisplay;

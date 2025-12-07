import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
// import HomepageFeatures from '@site/src/components/HomepageFeatures'; // We will replace this
import Heading from '@theme/Heading';

import styles from './index.module.css';

// Reusing HomepageHeader for the Hero Section
function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro"> {/* Link to the book's introduction */}
            Start Reading
          </Link>
          <Link
            className="button button--secondary button--lg"
            to="/docs/module1/week1/chapter-01-intro"> {/* Link to the first chapter of the first module */}
            Explore Modules
          </Link>
        </div>
      </div>
    </header>
  );
}

// New component for Key Features/Value Proposition
function KeyFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          <div className={clsx('col col--4')}>

            <Heading as="h3" className="text--center">Theoretical Foundations</Heading>
            <p className="text--center">Dive deep into the mathematical and scientific principles underpinning physical AI and robotics.</p>
          </div>
          <div className={clsx('col col--4')}>

            <Heading as="h3" className="text--center">Practical Implementations</Heading>
            <p className="text--center">Learn through hands-on code examples and real-world case studies for practical application.</p>
          </div>
          <div className={clsx('col col--4')}>

            <Heading as="h3" className="text--center">Cutting-Edge Research</Heading>
            <p className="text--center">Stay updated with the latest advancements and future trends in humanoid robotics and AI.</p>
          </div>
        </div>
      </div>
    </section>
  );
}

// New component for Course Structure/Learning Path Overview
function CourseStructure() {
  return (
    <section className={styles.courseStructure}>
      <div className="container">
        <Heading as="h2" className="text--center">Course Structure at a Glance</Heading>
        <div className="row">
          <div className={clsx('col col--3')}>
            <div className={styles.card}>
              <Heading as="h3">Module 1</Heading>
              <p>Foundations of Physical AI & Robotics</p>
            </div>
          </div>
          <div className={clsx('col col--3')}>
            <div className={styles.card}>
              <Heading as="h3">Module 2</Heading>
              <p>Robot Perception and Environmental Understanding</p>
            </div>
          </div>
          <div className={clsx('col col--3')}>
            <div className={styles.card}>
              <Heading as="h3">Module 3</Heading>
              <p>Autonomous Navigation and Manipulation</p>
            </div>
          </div>
          <div className={clsx('col col--3')}>
            <div className={styles.card}>
              <Heading as="h3">Module 4</Heading>
              <p>Advanced Humanoids and Ethical AI</p>
            </div>
          </div>
        </div>
        <div className="text--center" style={{ marginTop: '20px' }}>
          <Link
            className="button button--primary button--lg"
            to="/docs/intro"> {/* Link to Get Started or intro */}
            View Full Syllabus
          </Link>
        </div>
      </div>
    </section>
  );
}


export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Welcome to ${siteConfig.title}`}
      description="A comprehensive textbook on physical AI and humanoid robotics.">
      <HomepageHeader />
      <main>
        <KeyFeatures />
        <CourseStructure />
        {/* Potentially add more sections here */}
      </main>
    </Layout>
  );
}
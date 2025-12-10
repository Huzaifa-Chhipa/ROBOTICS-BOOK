import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Comprehensive Curriculum',
    Svg: require('@site/static/img/robotics_logo.svg').default,
    description: (
      <>
        From the fundamentals of kinematics and dynamics to advanced topics in
        perception and control, this book covers everything you need to know.
      </>
    ),
  },
  {
    title: 'Hands-On Learning',
    Svg: require('@site/static/img/robotics_logo.svg').default,
    description: (
      <>
        Reinforce your understanding with practical examples, coding exercises,
        and real-world case studies.
      </>
    ),
  },
  {
    title: 'For Students & Practitioners',
    Svg: require('@site/static/img/robotics_logo.svg').default,
    description: (
      <>
        Whether you're a student just starting out or a seasoned professional,
        this book is your go-to guide for robotics.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

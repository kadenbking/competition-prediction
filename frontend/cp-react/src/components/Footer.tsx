import React from "react";
import { Footer as FlowbiteFooter } from "flowbite-react";
import { FaGithub } from "react-icons/fa";

function Footer() {
  return (
    <FlowbiteFooter container={true}>
      <FlowbiteFooter.Copyright
        href="/"
        by="Competition Prediction"
        year={2022}
      />
      <FlowbiteFooter.LinkGroup>
        <FlowbiteFooter.Link href="#">
          <div className="flex flex-row my-5">
            <FlowbiteFooter.Icon icon={FaGithub} className="mx-2" />
            <span className="mx-2">View Our GitHub Repository</span>
          </div>
        </FlowbiteFooter.Link>
      </FlowbiteFooter.LinkGroup>
    </FlowbiteFooter>
  );
}

export default Footer;
